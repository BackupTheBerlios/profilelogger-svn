#ifndef TABLE_CONSTRAINT_H
#define TABLE_CONSTRAINT_H

#include "DbInterfacePartInTable.h"

class TableColumn;

class TableConstraint: public DbInterfacePartInTable
{
  Q_OBJECT
    public:
  TableConstraint(Table* t, const QString& name);
  virtual ~TableConstraint();

  void add(TableColumn* c) {
    _cols.append(c);
  }

  QList<TableColumn*>::iterator getFirstColumn() {
    return _cols.begin();
  }

  QList<TableColumn*>::iterator getLastColumn() {
    return _cols.end();
  }

 private:
  QList<TableColumn*> _cols;
};

#endif
