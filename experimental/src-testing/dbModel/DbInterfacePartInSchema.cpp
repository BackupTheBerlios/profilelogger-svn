#include "DbInterfacePartInSchema.h"

#include "Schema.h"

DbInterfacePartInSchema::DbInterfacePartInSchema(Schema* s, const QString& n)
  : DbInterfacePart(s, n)
{
}

DbInterfacePartInSchema::~DbInterfacePartInSchema()
{}

QString DbInterfacePartInSchema::getQualifiedName()
{
  return QString("%1.%2")
    .arg(getSchema()->getQualifiedName())
    .arg(getName());
}

Schema* DbInterfacePartInSchema::getSchema() {
  return static_cast<Schema*>(parent());
}

