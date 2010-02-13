#include "TransactionError.h"

TransactionError::TransactionError(const QSqlError& dbErr,
				   const QString& msg)
  : AbstractDatabaseError(msg),
    _dbErr(dbErr)
{}

QString TransactionError::text() const {
  if (!getMessage().isEmpty()) {
    return QString("%1: %2").arg(getMessage()).arg(_dbErr.text());
  } else {
    return _dbErr.text();
  }
}

