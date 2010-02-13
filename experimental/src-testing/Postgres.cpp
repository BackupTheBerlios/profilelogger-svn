#include "Postgres.h"

#include <QDebug>

#include "Table.h"
#include "TableColumn.h"
#include "Sequence.h"
#include "SqlFactory.h"

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
			       const QVariantList& values) {
  char** paramValues;
  paramValues = new char*[values.size()];

  for (int i = 0; i < values.size(); i++) {
    paramValues[i] = qstrdup(values.at(i).toString().toUtf8());
  }

  PGresult* ret = PQexecParams(_psql,
			       sql.toAscii().constData(),
			       values.size(),
			       NULL, // backend deduces param types
			       paramValues,
			       NULL, // params are text, no lengths required
			       NULL, // all params default to text
			       0); // ask for text

  delete[] paramValues;
  return ret;
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

void Postgres::execInsert(Table* t,
			  QList<TableColumn*> cols,
			  const QStringList& placeholders,
			  const QVariantList& values) {
  QStringList colNames;
  for (QList<TableColumn*>::iterator it = cols.begin(); it != cols.end(); it++) {
    colNames << (*it)->getName();
  }

  QString sql = QString("INSERT INTO %1(%2) VALUES(%3)")
    .arg(t->getQualifiedName())
    .arg(colNames.join(", "))
    .arg(placeholders.join(", "));

  PGresult* res = execParams(sql, values);

  if (PGRES_COMMAND_OK != PQresultStatus(res)) {
    QStringList params;
    for (int i = 0; i < values.size(); i++) {
      params << values.at(i).toString();
    }
    
    DatabaseError e(tr("Could not execute insert.\nParameters: \n\t%1")
		    .arg(params.join("\n\t")),
		    sql,
		    qstrdup(PQresultErrorMessage(res)));
    PQclear(res);
    throw e;
  }
}

void Postgres::execUpdate(Table* t,
			  QList<TableColumn*> updateCols,
			  const QStringList& updatePlaceholders,
			  const QVariantList& updateValues,
			  TableColumn* idCol,
			  const QString& idValuePlaceholder,
			  const int id) {
  QStringList kv;
  QVariantList values = updateValues;
  values << QVariant(id);

  for (int i = 0; i < updatePlaceholders.size(); i++) {
    kv << QString("%1 = %2")
      .arg(updateCols.at(i)->getName())
      .arg(updatePlaceholders.at(i));
  }

  QString sql = QString("UPDATE %1 SET %2 WHERE %3 = %4")
    .arg(t->getQualifiedName())
    .arg(kv.join(", "))
    .arg(idCol->getName())
    .arg(idValuePlaceholder);

  PGresult* res = execParams(sql, values);

  if (PGRES_COMMAND_OK != PQresultStatus(res)) {
    QStringList params;
    for (int i = 0; i < updateValues.size(); i++) {
      params << updateValues.at(i).toString();
    }
    
    DatabaseError e(tr("Could not execute update.\nParameters: \n\t%1\nValues:\n\t%2\nDataset ID: %3")
		    .arg(kv.join("\n\t"))
		    .arg(params.join("\n\t"))
		    .arg(id),
		    sql,
		    qstrdup(PQresultErrorMessage(res)));
    PQclear(res);
    throw e;
  }
}

void Postgres::declareSelectCursor(const QString& cursorName,
				   QList<TableColumn*> cols,
				   Table* t,
				   QList<TableColumn*> orderCols) {
  QStringList selectColNames;
  QStringList orderColNames;

  for (int i = 0; i < cols.size(); i++) {
    selectColNames << cols.at(i)->getName();
  }

  for (int i = 0; i < orderCols.size(); i++) {
    orderColNames << orderCols.at(i)->getName();
  }

  if (orderColNames.size() > 0) {
    declareCursor(cursorName, 
		  QString("SELECT %1 from %2 order by %3")
		  .arg(selectColNames.join(", "))
		  .arg(t->getQualifiedName())
		  .arg(orderColNames.join(", ")));
  } else {
    declareCursor(cursorName, 
		  QString("SELECT %1 from %2")
		  .arg(selectColNames.join(", "))
		  .arg(t->getQualifiedName()));
  }
}

void Postgres::createSchema(Database* db) {
  SqlFactory f(0);
  QStringList sql;

  sql << "DROP SCHEMA data CASCADE";

  for (QList<Schema*>::iterator it = db->getFirstSchema(); it != db->getLastSchema(); it++) {
    Schema* schema = *it;

    QStringList buf = f.make(schema);
    sql << buf;

    for (QList<Sequence*>::iterator seqIt = schema->getFirstSequence(); seqIt != schema->getLastSequence(); seqIt++) {
      sql << f.make(*seqIt);
    }
  }

  for (QList<Schema*>::iterator sit = db->getFirstSchema(); sit != db->getLastSchema(); sit++) {
    Schema* schema = *sit;

    for (QList<Table*>::iterator tit = schema->getFirstTable(); tit != schema->getLastTable(); tit++) {
      Table* table = *tit;
      sql << f.make(table);

      for (QList<UniqueConstraint*>::iterator ucit = table->getFirstUniqueConstraint(); ucit != table->getLastUniqueConstraint(); ucit++) {
        sql << f.make(*ucit);
      }
      for (QList<TextNotEmptyCheckConstraint*>::iterator cit = table->getFirstTextNotEmptyCheckConstraint(); cit != table->getLastTextNotEmptyCheckConstraint(); cit++
	   ) {
        sql << f.make(*cit);
      }
      if (table->hasPrimaryKey()) {
        sql << f.make(table->getPrimaryKey());
      }
    }
  }

  for (QList<Schema*>::iterator sit = db->getFirstSchema(); sit != db->getLastSchema(); sit++) {
    Schema* schema = *sit;

    for (QList<Table*>::iterator tit = schema->getFirstTable(); tit != schema->getLastTable(); tit++) {
      Table* table = *tit;

      for (QList<ForeignKey*>::iterator fkit = table->getFirstForeignKey(); fkit != table->getLastForeignKey(); fkit++) {
        sql << f.make(*fkit);
      }
      for(QList<TableColumn*>::iterator cit = table->getFirstTableColumn(); cit != table->getLastTableColumn(); cit++) {
        TableColumn* c = *cit;

        if (c->hasSequence()) {
          sql << f.makeDefaultFromSequence(c);
        }
        if (c->getHasDefaultText()) {
          sql << f.makeDefaultText(c);
        }
        if (c->getHasDefaultInt()) {
          sql << f.makeDefaultInt(c);
        }
        if (c->getHasDefaultDouble()) {
          sql << f.makeDefaultDouble(c);
        }

    
        if (c->getDefaultConstant() != Database::NOTHING) {
          sql << f.makeDefaultFromConstant(c);
        }
      }
    }
  }

  for (QStringList::iterator it = sql.begin(); it != sql.end(); it++) {
    exec(*it);
  }
}
