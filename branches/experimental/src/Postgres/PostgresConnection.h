#ifndef POSTGRES_CONNECTION_H
#define POSTGRES_CONNECTION_H

#include <QObject>

#include "PostgresConnectionSettings.h"

#include <libpq-fe.h>

#include <QMap>
#include <QList>
#include <QVariant>

class Database;
class Sequence;
class Table;
class TableColumn;

class PostgresConnection: public QObject
{
    Q_OBJECT
	public:
    PostgresConnection(QObject* p);
    virtual ~PostgresConnection();
    
    void clearResult(PGresult* res);
    void declareCursor(const QString& name,
		       const QString& sql);
    void declareSelectCursor(const QString& cursorName,
			     QList<TableColumn*> cols,
			     Table* t,
			     QList<TableColumn*> orderCols);
    void declareSelectByIdCursor(const QString& cursorName,
				 QList<TableColumn*> cols,
				 Table* t,
				 QList<TableColumn*> orderCols,
				 TableColumn* whereCol,
				 const int whereId);
    
    void dropSchema(Database* db);
    void createSchema(Database* db);
    
    void closeCursor(const QString& name);
    PGresult* fetchAllInCursor(const QString& name);
    PGresult* exec(const QString& cmd);
    PGresult* execParams(const QString& sql,
			 const QVariantList& values);
    QStringList getFieldNames(PGresult* res);
    int getRowCount(PGresult* res);
    int getFieldCount(PGresult* res);
    QList< QMap<QString, QVariant> > getData(PGresult* res);
    QMap<QString, QVariant> getRow(PGresult* res, int r);
    int nextval(Sequence* seq);
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

    QString errorString() const;

signals:
    void connectionEstablished(const QString& infoString);
    void connectionClosed();

    void startingTransaction();
    void transactionStarted();
    void transactionCommited();
    void commitingTransaction();
    void transactionRolledBack();
    void rollingBackTransaction();
    
    void preparingQuery(const QString& sql);
    void queryPrepared(const QString& sql);
    void executingQuery(const QString& sql);
    void queryExecuted(const QString& sql);
    
    public slots:
    void openDatabase(const PostgresConnectionSettings& s);
    void closeDatabase();
    void begin();
    void commit();
    void rollback();

private:
    PGconn* _conn;
};

#endif
