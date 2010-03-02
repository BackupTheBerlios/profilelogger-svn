#include "PostgresConnection.h"

#include "../DatabaseModel/Database.h"
#include "../DatabaseModel/Schema.h"
#include "../DatabaseModel/Sequence.h"
#include "../DatabaseModel/Table.h"
#include "../DatabaseModel/TableColumn.h"
#include "../DatabaseModel/ForeignKey.h"

#include "../SqlFactory/SqlFactory.h"

#include "DatabaseError.h"

PostgresConnection::PostgresConnection(QObject* p)
    : QObject(p),
      _conn(0)
{
}

PostgresConnection::~PostgresConnection()
{
    if (_conn) {
	PQfinish(_conn);
    }
}

QString PostgresConnection::errorString() const  {
  return PQerrorMessage(_conn);
}

void PostgresConnection::openDatabase(const PostgresConnectionSettings& s)
{
    _conn = PQconnectdb(qstrdup(s.makeConnectionString().toUtf8()));

    if (!_conn) {
	emit connectionClosed();
	throw DatabaseError(QString("%1: %2").arg("PQconnectdb returned NULL: ")
			    .arg(errorString()));
    }

    if (PQstatus(_conn) != CONNECTION_OK) {
	emit connectionClosed();
	QString dbMsg = errorString();
	PQfinish(_conn);
	throw DatabaseError(dbMsg);
    }
    
    emit connectionEstablished(QString("%1@%2:%3/%4")
			       .arg(s.getLogin())
			       .arg(s.getHost())
			       .arg(s.getPort())
			       .arg(s.getDatabase()));
}

PGresult* PostgresConnection::exec(const QString& cmd)  {
    emit executingQuery(cmd);
    
    const char* csql = qstrdup(cmd.toUtf8());

    PGresult* res = PQexec(_conn, csql);
    
    if (PQresultStatus(res) != PGRES_COMMAND_OK) {
	PQclear(res);
	throw DatabaseError(errorString());
    }
    
    emit queryExecuted(cmd);
    
    return res;
}

void PostgresConnection::closeDatabase()
{
    PQfinish(_conn);
    emit connectionClosed();
}

void PostgresConnection::clearResult(PGresult* res) 
{
    if (res) {
	PQclear(res);
    }
}

void PostgresConnection::declareCursor(const QString& cursorName,
				       const QString& sql) 
{
    PGresult* res =  exec(QString("DECLARE %1 CURSOR FOR %2")
			  .arg(cursorName)
			  .arg(sql));
    clearResult(res);
}

void PostgresConnection::closeCursor(const QString& cursorName)
{
    PGresult* res = exec(QString("CLOSE %1").arg(cursorName));
    clearResult(res);
}

PGresult* PostgresConnection::fetchAllInCursor(const QString& cursorName) {
    QString cmd = QString("FETCH ALL IN %1").arg(cursorName);
    PGresult* res = PQexec(_conn, cmd.toAscii().constData());
    
    if (PQresultStatus(res) != PGRES_TUPLES_OK) {
	PQclear(res);
	throw DatabaseError(errorString());
    }
    
    return res;
}

void PostgresConnection::begin()
{
    emit startingTransaction();
    PGresult *res = exec("BEGIN");
    clearResult(res);
    emit transactionStarted();
}

void PostgresConnection::commit() 
{
    emit commitingTransaction();
    PGresult *res = exec("COMMIT");
    clearResult(res);
    emit transactionCommited();
}

void PostgresConnection::rollback()
{
    emit rollingBackTransaction();
    PGresult *res = exec("ROLLBACK");
    clearResult(res);
    emit transactionRolledBack();
}
QStringList PostgresConnection::getFieldNames(PGresult* res) {
    QStringList ret;
    int nFields = getFieldCount(res);

    for (int i = 0; i < nFields; i++) {
	ret << PQfname(res, i);
    }

    return ret;
}


int PostgresConnection::getRowCount(PGresult* res) {
    return PQntuples(res);
}

int PostgresConnection::getFieldCount(PGresult* res) {
    return PQnfields(res);
}

QList< QMap<QString, QVariant> > PostgresConnection::getData(PGresult* res) 
{
    int rows = getRowCount(res);

    QList< QMap<QString, QVariant> > ret;

    for (int r = 0; r < rows; r++) {
	ret << getRow(res, r);
    }
  
    return ret;
}

QMap<QString, QVariant> PostgresConnection::getRow(PGresult* res, int r) {
    QStringList fields = getFieldNames(res);
    QMap<QString, QVariant> ret;

    for (int c = 0; c < fields.size(); c++) {
	ret[fields.at(c)] = PQgetvalue(res, r, c);
    }

    return ret;
}



PGresult* PostgresConnection::execParams(const QString& sql,
					 const QVariantList& values) {
    char** paramValues;
    paramValues = new char*[values.size()];

    for (int i = 0; i < values.size(); i++) {
	paramValues[i] = qstrdup(values.at(i).toString().toUtf8());
    }

    const char* csql = qstrdup(sql.toUtf8());

    PGresult* ret = PQexecParams(_conn,
				 csql,
				 values.size(),
				 NULL, // backend deduces param types
				 paramValues,
				 NULL, // params are text, no lengths required
				 NULL, // all params default to text
				 0); // ask for text

    delete[] paramValues;
    return ret;
}

int PostgresConnection::nextval(Sequence* s) {
    QString cmd = QString("SELECT NEXTVAL('%1') AS nv").arg(s->getQualifiedName());

    PGresult* res = PQexec(_conn, cmd.toAscii().constData());

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

void PostgresConnection::execInsert(Table* t,
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

void PostgresConnection::execUpdate(Table* t,
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

void PostgresConnection::declareSelectByIdCursor(const QString& cursorName,
				   QList<TableColumn*> cols,
				   Table* t,
				   QList<TableColumn*> orderCols,
				   TableColumn* whereCol,
				   const int whereId) {
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
		  QString("SELECT %1 from %2 WHERE %3 = %4 order by %5")
		  .arg(selectColNames.join(", "))
		  .arg(t->getQualifiedName())
		  .arg(whereCol->getName())
		  .arg(whereId)
		  .arg(orderColNames.join(", ")));
  } else {
    declareCursor(cursorName, 
		  QString("SELECT %1 from %2 where %3 = %4")
		  .arg(selectColNames.join(", "))
		  .arg(whereCol->getName())
		  .arg(whereId)
		  .arg(t->getQualifiedName()));
  }
}

void PostgresConnection::declareSelectCursor(const QString& cursorName,
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


void PostgresConnection::dropSchema(Database* db) {
    SqlFactory f(0);
    QStringList sql;

    for (QList<Schema*>::iterator it = db->getFirstSchema(); it != db->getLastSchema(); it++) {
	sql << f.drop(*it, true);
    }

    for (QStringList::iterator it = sql.begin(); it != sql.end(); it++) {
	exec(*it);
    }
}


void PostgresConnection::createSchema(Database* db) {
    SqlFactory f(0);
    QStringList sql;

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
