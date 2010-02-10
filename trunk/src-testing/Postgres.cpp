#include "Postgres.h"

#include <QDebug>

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

QMap<QString, QVariant> Postgres::getRow(PGresult* res, int r) {
  QStringList fields = getFieldNames(res);
  QMap<QString, QVariant> ret;

  for (int c = 0; c < fields.size(); c++) {
    ret[fields.at(c)] = PQgetvalue(res, r, c);
  }

  return ret;
}
