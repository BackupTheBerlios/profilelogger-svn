#include "QueryError.h"

#include <QStringList>

QueryError::QueryError(const QSqlError& dbErr,
			     const QSqlError& qErr,
			     const QString& msg)
  : AbstractDatabaseError(msg),
    _dbErr(dbErr),
    _qErr(qErr)
{}

QString QueryError::text() const {
  QStringList ret;
  if (!getMessage().isEmpty()) {
    ret << getMessage();
  } else {
    ret << tr("A Database Error Occured:");
  }

  ret << tr("Database Message: %1").arg(_dbErr.text())
      << tr("Query Message: %1").arg(_qErr.text());

  return ret.join("\n");
}
