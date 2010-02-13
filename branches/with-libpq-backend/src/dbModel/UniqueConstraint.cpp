#include "UniqueConstraint.h"

UniqueConstraint::UniqueConstraint(Table* t, const QString& name)
  : TableConstraint(t, name)
{}

UniqueConstraint::~UniqueConstraint()
{}

