#include "TableConstraint.h"

TableConstraint::TableConstraint(Table* t, const QString& n)
  : DbInterfacePartInTable(t, n)
{}

TableConstraint::~TableConstraint()
{}
