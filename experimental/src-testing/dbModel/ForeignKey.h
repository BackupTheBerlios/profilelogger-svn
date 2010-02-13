#ifndef FOREIGN_KEY_H
#define FOREIGN_KEY_H

#include "TableConstraint.h"

class TableColumn;

class ForeignKey: public TableConstraint
{
  Q_OBJECT
    public:
  ForeignKey(Table* t, const QString& name);
  virtual ~ForeignKey();

  void setColumns(TableColumn* l, TableColumn* r) {
    _local = l;
    _referenced = r;
  }

  TableColumn* getLocalColumn() const {
    return _local;
  }

  TableColumn* getReferencedColumn() const {
    return _referenced;
  }

 private:
  TableColumn* _local;
  TableColumn* _referenced;
};

#endif
