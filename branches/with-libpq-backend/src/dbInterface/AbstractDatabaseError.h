#ifndef ABSTRACT_DATABASE_ERROR_H
#define ABSTRACT_DATABASE_ERROR_H

#include <QCoreApplication>
#include <QString>

class AbstractDatabaseError {
  Q_DECLARE_TR_FUNCTIONS(AbstractDatabaseError)

    public:
  AbstractDatabaseError(const QString& msg = tr("Abstract Database Error"));
  virtual ~AbstractDatabaseError() {}

  virtual QString text() const;

 protected:
  QString getMessage() const {
    return _msg;
  }

 private:
  QString _msg;
};

#endif
