#ifndef _DATABASE_CONNECTION_H
#define _DATABASE_CONNECTION_H

#include <QObject>

#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlError>
#include <QMap>

class DatabaseConnection: public QObject {
  Q_OBJECT
    public:
  DatabaseConnection(QObject* p);
  virtual ~DatabaseConnection();

  QSqlQuery createQuery(const QString& sql);
  void prepare(QSqlQuery* q);
  void bindValue(QSqlQuery* q, const QString& placeholder, QVariant value);
  void bindValues(QSqlQuery* q, QStringList placeholders, QList<QVariant> values);

  void execSelect(QSqlQuery* q, int expectedSize = 0);
  void execInsert(QSqlQuery* q, int expectedAffectedRows = 1);
  void execUpdate(QSqlQuery* q, int expectedAffectedRows = 1);
  void execDelete(QSqlQuery* q, int expectedAffectedRows = 1);

  void execDDL(const QString& sql);

  bool begin();
  bool commit();
  bool rollback();
  QSqlError getLastError();

  bool ping();

  public slots:
  virtual void slotOpen(const QString& pass);
  virtual void slotClose();

 signals:
  void connectionEstablished(const QString& connectionString);
  void connectionClosed();
  void connectionLost();
  void connectionList(const QString& connectionString);
  void preparingQuery(const QString& sql);
  void executingQuery(const QString& sql);
  void queryPrepared(const QString& sql);
  void queryExecuted(const QString& sql);

 private:
  void dropSchemas();
  void createSchemas();
  void insertTemplateData();

  QSqlDatabase _defaultDb;

  QMap<QString, QSqlQuery> _prepared;
};

#endif
