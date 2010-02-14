#include "DataManager.h"

#include "Postgres.h"

#include "Dataset.h"

#include "Table.h"
#include "TableColumn.h"
#include "SqlFactory.h"

#include "libpq-fe.h"

DataManager::DataManager(QObject* p, Postgres* pg, ProfileLoggerDatabase* dm)
  : QObject(p),
    _pg(pg),
    _dm(dm),
    _sqlF(0)
{
  _sqlF = new SqlFactory(this);
}

void DataManager::remove(Dataset* d) {
  QString sql = QString("DELETE FROM %1 WHERE %2 = $1::%3")
    .arg(getTable()->getQualifiedName())
    .arg(getTable()->getIdColumn()->getName())
    .arg(getSqlFactory()->typeToString(getTable()->getIdColumn()->getDataType()));

  QVariantList params;
  params << d->getId();

  PGresult* res = getPostgres()->execParams(sql, params);
  
  if (PGRES_COMMAND_OK != PQresultStatus(res)) {
    throw DatabaseError(tr("Could not delete project '%1'.").arg(d->toString()),
			sql,
			PQresultErrorMessage(res));
  }
}

QString DataManager::makePlaceholder(const int placeholderNumber, TableColumn* col) const
{
  return QString("$%1::%2")
    .arg(placeholderNumber)
    .arg(getSqlFactory()->typeToString(col->getDataType()));
}

void DataManager::performInsert(Table* t,
				QList<TableColumn*> cols,
				const QStringList& placeholders,
				const QVariantList& values) {
  getPostgres()->execInsert(t, 
			    cols, 
			    placeholders,
			    values);
}

void DataManager::performUpdate(Table* t,
				QList<TableColumn*> updateCols,
				const QStringList& updatePlaceholders,
				const QVariantList& updateValues,
				TableColumn* idCol,
				const QString& idPlaceholder,
				const int id) {
  getPostgres()->execUpdate(t,
			    updateCols,
			    updatePlaceholders,
			    updateValues,
			    idCol,
			    idPlaceholder,
			    id);
}

QList< QMap<QString, QVariant> > DataManager::loadDataWithCursor(const QString& cursorName,
								 QList<TableColumn*> cols,
								 Table* t,
								 QList<TableColumn*> sortCols) {
  getPostgres()->declareSelectCursor(cursorName, 
				     cols,
				     t,
				     sortCols);

  PGresult* res = getPostgres()->fetchAllInCursor(cursorName);

  QList< QMap<QString, QVariant> > ret = getPostgres()->getData(res);

  getPostgres()->closeCursor(cursorName);
  getPostgres()->clearResult(res);

  return ret;
}
