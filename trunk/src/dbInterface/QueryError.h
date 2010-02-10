#ifndef QUERY_ERROR_H
#define QUERY_ERROR_H

#include <QSqlError>

#include "AbstractDatabaseError.h"

class QueryError: public AbstractDatabaseError {
  Q_DECLARE_TR_FUNCTIONS(QueryError)

 public:
  QueryError(const QSqlError& dbErr,
		const QSqlError& qErr,
		const QString& msg);
  virtual ~QueryError() {}

  virtual QString text() const;

 private:
  QSqlError _dbErr;
  QSqlError _qErr;
};

#endif
