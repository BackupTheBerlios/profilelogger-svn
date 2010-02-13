#include "DbInterfacePartInTable.h"

#include "Table.h"

DbInterfacePartInTable::DbInterfacePartInTable(Table* t, const QString& name)
  : DbInterfacePart(t, name)
{}

DbInterfacePartInTable::~DbInterfacePartInTable()
{}

QString DbInterfacePartInTable::getQualifiedName()
{
  return QString("%1.%2").arg(getTable()->getName()).arg(getName());
}

Table* DbInterfacePartInTable::getTable()
{
  return static_cast<Table*>(parent());
}

