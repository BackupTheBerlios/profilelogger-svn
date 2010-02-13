#ifndef DB_INTERFACE_PART_IN_SCHEMA_H
#define DB_INTERFACE_PART_IN_SCHEMA_H

#include "DbInterfacePart.h"

class Table;

class DbInterfacePartInTable: public DbInterfacePart
{
  Q_OBJECT
    public:
  DbInterfacePartInTable(Table* t, const QString& name);
  virtual ~DbInterfacePartInTable();
  virtual QString getQualifiedName();
  Table* getTable();
};

#endif
