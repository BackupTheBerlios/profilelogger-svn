#include "DatabaseConnection.h"

#include <QApplication>
#include <QMessageBox>
#include <QDebug>
#include <QSqlError>
#include <QSqlRecord>

#include "ProfileLogger.h"
#include "Settings.h"
#include "DatabaseConnectionSettings.h"
#include "SqlFactory.h"
#include "ProfileLoggerDatabase.h"
#include "QueryError.h"
#include "TransactionError.h"
#include "ConnectionError.h"

#include "Database.h"
#include "Schema.h"
#include "Sequence.h"
#include "Table.h"
#include "TableColumn.h"
#include "UniqueConstraint.h"
#include "PrimaryKey.h"
#include "TextNotEmptyCheckConstraint.h"


DatabaseConnection::DatabaseConnection(QObject* p)
  : QObject(p)
{}

DatabaseConnection::~DatabaseConnection()
{
  slotClose();
}

void DatabaseConnection::slotOpen(const QString& pass) {
  DatabaseConnectionSettings s = (static_cast<ProfileLogger*>(QApplication::instance()))->getSettings()->getDatabaseConnectionSettings();

  _defaultDb = QSqlDatabase::addDatabase("QPSQL");
  _defaultDb.setHostName(s.getHost());
  _defaultDb.setPort(s.getPort());
  _defaultDb.setDatabaseName(s.getDatabase());
  _defaultDb.setUserName(s.getUser());
  _defaultDb.setPassword(pass);

  if (!_defaultDb.open()) {
    throw ConnectionError(_defaultDb.lastError(),
			  tr("Could Not Connect To Database"));
  }
 
  ping();

  emit connectionEstablished(s.makeConnectionString());

  if (s.getDropSchema()) {
    dropSchemas();
  }
  if (s.getCreateSchema()) {
    createSchemas();
  }
  if (s.getInsertTemplateData()) {
    insertTemplateData();
  }
}

void DatabaseConnection::slotClose() {
  if (_defaultDb.isOpen()) {
    QSqlDatabase::removeDatabase("default");
    _defaultDb.close();
    emit connectionClosed();
  }
}

QSqlQuery DatabaseConnection::createQuery(const QString& sql) {
  return QSqlQuery(sql, _defaultDb);
}

void DatabaseConnection::prepare(QSqlQuery* q) {
  if (!q) {
    throw QueryError(_defaultDb.lastError(),
		     _defaultDb.lastError(),
		     tr("Query Pointer in DatabaseConnection::prepare(...) is Null."));
  }

  QString sql = q->lastQuery();

  if (!q->prepare(sql)) {
    throw QueryError(_defaultDb.lastError(),
		     q->lastError(),
		     tr("Could not prepare Query."));
  }
}

void DatabaseConnection::exec(QSqlQuery* q) {
  if (!q->exec()) {
    throw QueryError(_defaultDb.lastError(),
		     q->lastError(),
		     tr("Could not exec query: %1").arg(q->lastQuery()));
  }
}

void DatabaseConnection::exec(QSqlQuery* q, 
			      QStringList placeholders, 
			      QList<QVariant> values) {
  if (!q) {
    return;
  }

  if (placeholders.size() != values.size()) {
    return;
  }

  for (int i = 0; i < placeholders.size(); i++) {
    QString key = placeholders.at(i);
    QVariant value = values.at(i);
    q->bindValue(key, value);
  }
}

void DatabaseConnection::execDDL(const QString& sql) {
  QSqlQuery q = createQuery(sql);
  exec(&q);
}

void DatabaseConnection::dropSchemas() {

  SqlFactory* f = new SqlFactory(this);
  QStringList ddl;

  ProfileLoggerDatabase* db = (static_cast<ProfileLogger*>(QApplication::instance()))->getProfileLoggerDatabase();

  for (QList<Schema*>::iterator it = db->getFirstSchema(); it != db->getLastSchema(); it++) {
    QStringList buf = f->drop(*it);
    ddl << buf;
  }

  begin();
  for (QStringList::iterator sql = ddl.begin(); sql != ddl.end(); sql++) {
    QSqlQuery q;

    if (!q.exec(*sql)) {
      rollback();
      throw QueryError(_defaultDb.lastError(),
		       q.lastError(),
		       tr("Execution of DDL Statement '%1' failed.").arg(*sql));
    }
  }
  commit();
}

void DatabaseConnection::createSchemas() {
  SqlFactory* f = new SqlFactory(this);
  QStringList ddl;

  ProfileLoggerDatabase* db = (static_cast<ProfileLogger*>(QApplication::instance()))->getProfileLoggerDatabase();

  for (QList<Schema*>::iterator it = db->getFirstSchema(); it != db->getLastSchema(); it++) {
    Schema* schema = *it;

    QStringList buf = f->make(schema);
    ddl << buf;

    for (QList<Sequence*>::iterator seqIt = schema->getFirstSequence(); seqIt != schema->getLastSequence(); seqIt++) {
      ddl << f->make(*seqIt);
    }
  }

  for (QList<Schema*>::iterator sit = db->getFirstSchema(); sit != db->getLastSchema(); sit++) {
    Schema* schema = *sit;

    for (QList<Table*>::iterator tit = schema->getFirstTable(); tit != schema->getLastTable(); tit++) {
      Table* table = *tit;
      ddl << f->make(table);

      for (QList<UniqueConstraint*>::iterator ucit = table->getFirstUniqueConstraint(); ucit != table->getLastUniqueConstraint(); ucit++) {
	ddl << f->make(*ucit);
      }
      for (QList<TextNotEmptyCheckConstraint*>::iterator cit = table->getFirstTextNotEmptyCheckConstraint(); cit != table->getLastTextNotEmptyCheckConstraint(); cit++) {
	ddl << f->make(*cit);
      }
      if (table->hasPrimaryKey()) {
	ddl << f->make(table->getPrimaryKey());
      }
    }
  }

  for (QList<Schema*>::iterator sit = db->getFirstSchema(); sit != db->getLastSchema(); sit++) {
    Schema* schema = *sit;

    for (QList<Table*>::iterator tit = schema->getFirstTable(); tit != schema->getLastTable(); tit++) {
      Table* table = *tit;

      for (QList<ForeignKey*>::iterator fkit = table->getFirstForeignKey(); fkit != table->getLastForeignKey(); fkit++) {
	ddl << f->make(*fkit);
      }
    }
  }

  begin();
  QSqlQuery q;
  for (QStringList::iterator sql = ddl.begin(); sql != ddl.end(); sql++) {
    if (!q.exec(*sql)) {
      rollback();
      throw QueryError(_defaultDb.lastError(),
		       q.lastError(),
		       tr("Execution of DDL Statement '%1' failed.").arg(*sql));
    }
  }
  commit();
}

void DatabaseConnection::insertTemplateData() {
}

bool DatabaseConnection::begin() {
  bool ret = _defaultDb.transaction();

  if (!ret) {
    throw TransactionError(_defaultDb.lastError(), tr("Could not BEGIN transaction."));
  }

  return ret;
}

bool DatabaseConnection::commit() {
  bool ret = _defaultDb.commit();

  if (!ret) {
    throw TransactionError(_defaultDb.lastError(), tr("Could not COMMIT transaction."));
  }

  return ret;
}

bool DatabaseConnection::rollback() {
  bool ret = _defaultDb.rollback();

  if (!ret) {
    throw TransactionError(_defaultDb.lastError(), tr("Could not ROLLBACK transaction."));
  }

  return ret;
}

QSqlError DatabaseConnection::getLastError() {
  return _defaultDb.lastError();
}

bool DatabaseConnection::ping() {
  QSqlQuery q;
  
  if (!q.exec("SELECT CURRENT_TIMESTAMP AS CURR_TS")) {
    throw QueryError(_defaultDb.lastError(),
		     q.lastError(),
		     tr("Could not ping database."));
  } else {
    q.first();
    QSqlRecord r = q.record();
    int idx = r.indexOf("CURR_TS");

    qDebug() << "ping result: " << r.value(idx).toString();
    return true;
  }
}
