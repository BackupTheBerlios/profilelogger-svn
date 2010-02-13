#ifndef ABSTRACTDATABASEERROR_H
#define ABSTRACTDATABASEERROR_H

#include <exception>

#include <QString>

class AbstractDatabaseError: public std::exception {
 public:
  AbstractDatabaseError(const QString& dbMsg);
  virtual ~AbstractDatabaseError() throw();

  QString getDatabaseMessage() const {
    return _dbMsg;
  }

  virtual QString text() const { 
    return getDatabaseMessage();
  }

 private:
  QString _dbMsg;
};

#endif
