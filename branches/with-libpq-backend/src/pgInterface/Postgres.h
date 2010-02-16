#ifndef POSTGRES_H
#define POSTGRES_H

#include <QObject>

#include <QString>
#include <QStringList>
#include <QList>
#include <QVariant>

#include <libpq-fe.h>

#include "DatabaseError.h"

#include "DatabaseConnectionSettings.h"

class Database;
class Table;
class TableColumn;
class Sequence;

class Postgres: public QObject {
  Q_OBJECT
    public:
  Postgres(QObject* p);
  virtual ~Postgres();
 
  void createSchema(Database* m);
  void dropSchema(Database* m);
  void insertTemplateData();

  QString errorString() const;

  PGresult* exec(const QString& cmd);

  void declareCursor(const QString& cursorName,
		     const QString& sql);

  void declareSelectCursor(const QString& cursorName,
			   QList<TableColumn*> cols,
			   Table* t,
			   QList<TableColumn*> orderCols);

  void declareSelectCursor(const QString& cursorName,
			   QList<TableColumn*> cols,
			   Table* t,
			   QList<TableColumn*> orderCols,
			   TableColumn* whereCol,
			   const int whereId);

  PGresult* fetchAllInCursor(const QString& cursorName);

  void closeCursor(const QString& cursorName);

  PGresult* execParams(const QString& sql, 
		       const QVariantList& values);

  void execInsert(Table* t,
		  QList<TableColumn*> cols,
		  const QStringList& placeholders,
		  const QVariantList& values);

  void execUpdate(Table* t,
		  QList<TableColumn*> updateCols,
		  const QStringList& updatePlaceholders,
		  const QVariantList& updateValues,
		  TableColumn* idCol,
		  const QString& idValuePlaceholder,
		  const int id);

  QStringList getFieldNames(PGresult* res);

  int getFieldCount(PGresult* res);

  int getRowCount(PGresult* res);

  QList< QMap<QString, QVariant> > getData(PGresult* res);

  QMap<QString, QVariant> getRow(PGresult* res, int r);

  void begin();
  void commit();
  void rollback();
  int nextval(Sequence* s);
  void open(const DatabaseConnectionSettings& s);
  void close();
  void clearResult(PGresult* res);

 signals:
  void connectionEstablished(const QString& conn);
  void connectionClosed();
  void connectionLost();

 private:
  PGconn* _psql;
};

#endif
