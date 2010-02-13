#include "CheckConstraint.h"

CheckConstraint::CheckConstraint(Table* t, const QString& name)
  : TableConstraint(t, name)
{}

CheckConstraint::~CheckConstraint()
{}
