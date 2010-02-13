#ifndef DATABASEERROR_H
#define DATABASEERROR_H

#include <QString>
#include <QList>
#include <QVariant>
#include <QStringList>

#include "libpq-fe.h"

#include "AbstractDatabaseError.h"

class DatabaseError: public AbstractDatabaseError {
 public:
  DatabaseError(const QString& msg,
		const QString& sql = QString::null,
		const QString& dbMsg = QString::null);

  virtual ~DatabaseError() throw();

  QString text() const {
    return QString("Message: %1\nSQL: \n\t%2\nDatabase Message: %3")
      .arg(_msg)
      .arg(_sql)
      .arg(getDatabaseMessage());
  }
 private:
  QString _sql;
  QString _msg;
};

#endif
