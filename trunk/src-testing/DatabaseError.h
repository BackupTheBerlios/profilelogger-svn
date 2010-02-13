#ifndef DATABASEERROR_H
#define DATABASEERROR_H

#include <QString>
#include <QList>
#include <QVariant>
#include <QStringList>

#include "libpq-fe.h"

class DatabaseError {
 public:
  DatabaseError(const QString& msg,
		const QString& sql = QString::null,
		const QString& dbMsg = QString::null);
  QString text() {

    return QString("Message: %1\nSQL: \n\t%2\nDatabase Message: %3")
      .arg(_msg)
      .arg(_sql)
      .arg(_dbMsg);
  }
 private:
  QString _msg;
  QString _sql;
  QString _dbMsg;
};

#endif
