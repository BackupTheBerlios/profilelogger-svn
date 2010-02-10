#ifndef DATABASEERROR_H
#define DATABASEERROR_H

#include <QString>

class DatabaseError {
 public:
  DatabaseError(const QString& msg);
  QString text() {
    return _msg;
  }
 private:
  QString _msg;
};

#endif
