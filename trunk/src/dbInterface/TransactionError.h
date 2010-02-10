#ifndef TRANSACTION_ERROR_H
#define TRANSACTION_ERROR_H

#include "AbstractDatabaseError.h"

#include <QSqlError>

class TransactionError: public AbstractDatabaseError {
   Q_DECLARE_TR_FUNCTIONS(TransactionError)

     public:
  TransactionError(const QSqlError& dbErr,
		   const QString& msg);
  virtual ~TransactionError() {}

  virtual QString text() const;

 private:
  QSqlError _dbErr;
};

#endif
