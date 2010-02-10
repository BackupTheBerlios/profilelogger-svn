#ifndef POSTGRES_H
#define POSTGRES_H

#include <QObject>

#include <QString>
#include <QStringList>
#include <QList>
#include <QVariant>

#include <libpq-fe.h>

#include "DatabaseError.h"

class Postgres: public QObject {
  Q_OBJECT
    public:
  Postgres(QObject* p);
  virtual ~Postgres();
 
  QString errorString() const;
  PGresult* exec(const QString& cmd);
  void declareCursor(const QString& cursorName,
		     const QString& sql);
  PGresult* fetchAllInCursor(const QString& cursorName);
  void closeCursor(const QString& cursorName);

  QStringList getFieldNames(PGresult* res);
  int getFieldCount(PGresult* res);
  int getRowCount(PGresult* res);
  QMap<QString, QVariant> getRow(PGresult* res, int r);

  void begin();
  void commit();
  void rollback();
  void connect(const QString& connStr = "hostaddr = '192.168.196.133' port = '5432' dbname = 'profilelogger' user = 'jolo' password = 'nix' connect_timeout = '10'");
  void close();
  void clearResult(PGresult* res);

 private:
  PGconn* _psql;
};

#endif
