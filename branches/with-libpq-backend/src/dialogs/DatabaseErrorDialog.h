#ifndef DATABASEERRORDIALOG_H
#define DATABASEERRORDIALOG_H

#include <QMessageBox>

#include "DatabaseError.h"

class DatabaseErrorDialog: public QMessageBox {
  Q_OBJECT
    public:
  DatabaseErrorDialog(QWidget* p, const DatabaseError& e);
  virtual ~DatabaseErrorDialog() {}
};

#endif
