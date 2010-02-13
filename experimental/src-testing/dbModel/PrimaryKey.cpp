#include "PrimaryKey.h"

PrimaryKey::PrimaryKey(Table* t, const QString& name)
  : TableConstraint(t, name)
{}

PrimaryKey::~PrimaryKey()
{}
