#ifndef _DB_INTERFACE_PART_IN_SCHEMA_H
#define _DB_INTERFACE_PART_IN_SCHEMA_H

#include "DbInterfacePart.h"

class Schema;

class DbInterfacePartInSchema: public DbInterfacePart
{
  Q_OBJECT
    public:
  DbInterfacePartInSchema(Schema* s, const QString& n);
  virtual ~DbInterfacePartInSchema();
  Schema* getSchema();
  virtual QString getQualifiedName();
};

#endif
