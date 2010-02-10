#ifndef CONNECTION_ERROR_H
#define CONNECTION_ERROR_H

#include "AbstractDatabaseError.h"

#include <QSqlError>

class ConnectionError: public AbstractDatabaseError {
  Q_DECLARE_TR_FUNCTIONS(ConnectionError)

    public:
  ConnectionError(const QSqlError& dbErr,
		  const QString& msg);
  virtual ~ConnectionError() {}

  virtual QString text() const;

 private:
  QSqlError _dbErr;
};

#endif
