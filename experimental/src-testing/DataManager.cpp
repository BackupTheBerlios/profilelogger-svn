#include "DataManager.h"

#include "Postgres.h"

#include "Dataset.h"

#include "Table.h"
#include "TableColumn.h"
#include "SqlFactory.h"

#include "libpq-fe.h"

DataManager::DataManager(QObject* p, Postgres* pg, AppDatabase* dm)
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
