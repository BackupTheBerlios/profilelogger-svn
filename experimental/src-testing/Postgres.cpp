#include "Postgres.h"

#include <QDebug>

#include "Project.h"
#include "Sequence.h"

Postgres::Postgres(QObject* p)
  : QObject(p)
{}

Postgres::~Postgres() {
  PQfinish(_psql);
}
 
QString Postgres::errorString() const  {
  return PQerrorMessage(_psql);
}

PGresult* Postgres::exec(const QString& cmd)  {
  qDebug() << cmd;
  PGresult* res = PQexec(_psql, cmd.toAscii().constData());

  if (PQresultStatus(res) != PGRES_COMMAND_OK) {
    PQclear(res);
    throw DatabaseError(errorString());
  }

  return res;
}

void Postgres::begin() {
  PQclear(exec("BEGIN"));
}

void Postgres::commit() {
  PQclear(exec("COMMIT"));
}

void Postgres::rollback() {
  PQclear(exec("ROLLBACK"));
}

void Postgres::connect(const QString& connStr) {
  _psql = PQconnectdb(connStr.toAscii().constData());

  if (!_psql) {
    throw DatabaseError(QString("%1: %2").arg("PQconnectdb returned NULL: ")
			.arg(errorString()));
  }

  if (PQstatus(_psql) != CONNECTION_OK) {
    close();
    throw DatabaseError(errorString());
  }
}

void Postgres::close() {
}

void Postgres::clearResult(PGresult* res) {
  if (res) {
    PQclear(res);
  }
}

void Postgres::declareCursor(const QString& cursorName,
			     const QString& sql) {
  PGresult* res =  exec(QString("DECLARE %1 CURSOR FOR %2")
			.arg(cursorName)
			.arg(sql));
  clearResult(res);
}

void Postgres::closeCursor(const QString& cursorName) {
  PGresult* res = exec(QString("CLOSE %1").arg(cursorName));
  clearResult(res);
}

PGresult* Postgres::fetchAllInCursor(const QString& cursorName) {
  QString cmd = QString("FETCH ALL IN %1").arg(cursorName);
  qDebug() << cmd;
  PGresult* res = PQexec(_psql, cmd.toAscii().constData());

  if (PQresultStatus(res) != PGRES_TUPLES_OK) {
    PQclear(res);
    throw DatabaseError(errorString());
  }

  return res;
}

QStringList Postgres::getFieldNames(PGresult* res) {
  QStringList ret;
  int nFields = getFieldCount(res);

  for (int i = 0; i < nFields; i++) {
    ret << PQfname(res, i);
  }

  return ret;
}

int Postgres::getRowCount(PGresult* res) {
  return PQntuples(res);
}

int Postgres::getFieldCount(PGresult* res) {
  return PQnfields(res);
}

QList< QMap<QString, QVariant> > Postgres::getData(PGresult* res) 
{
  int rows = getRowCount(res);

  QList< QMap<QString, QVariant> > ret;

  for (int r = 0; r < rows; r++) {
    ret << getRow(res, r);
  }
  
  return ret;
}

QMap<QString, QVariant> Postgres::getRow(PGresult* res, int r) {
  QStringList fields = getFieldNames(res);
  QMap<QString, QVariant> ret;

  for (int c = 0; c < fields.size(); c++) {
    ret[fields.at(c)] = PQgetvalue(res, r, c);
  }

  return ret;
}

PGresult* Postgres::execParams(const QString& sql, 
			       int paramCount,
			       const char* const *paramValues) {
  return PQexecParams(_psql,
		      sql.toAscii().constData(),
		      paramCount,
		      NULL, // backend deduces param types
		      paramValues,
		      NULL, // params are text, no lengths required
		      NULL, // all params default to text
		      0); // ask for text
}

int Postgres::nextval(Sequence* s) {
  QString cmd = QString("SELECT NEXTVAL('%1') AS nv").arg(s->getQualifiedName());

  PGresult* res = PQexec(_psql, cmd.toAscii().constData());

  if (PQresultStatus(res) != PGRES_TUPLES_OK) {
    QString msg1 = errorString();
    QString msg2 = PQresultErrorMessage(res);
    PQclear(res);
    throw DatabaseError(msg1,
			cmd,
			msg2);
  }

  QMap<QString, QVariant> r = getRow(res, 0);
  return r["nv"].toInt();
}
