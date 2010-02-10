#ifndef DATABASEERRORDIALOG_H
#define DATABASEERRORDIALOG_H

#include <QMessageBox>

#include "QueryError.h"
#include "TransactionError.h"
#include "ConnectionError.h"

class DatabaseErrorDialog: public QMessageBox {
  Q_OBJECT
    public:
  DatabaseErrorDialog(QWidget* p, const QueryError& e);
  DatabaseErrorDialog(QWidget* p, const TransactionError& e);
  DatabaseErrorDialog(QWidget* p, const ConnectionError& e);
  virtual ~DatabaseErrorDialog() {}
};

#endif
