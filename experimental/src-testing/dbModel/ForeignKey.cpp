#include "ForeignKey.h"

ForeignKey::ForeignKey(Table* t, const QString& name)
  : TableConstraint(t, name)
{}

ForeignKey::~ForeignKey()
{}
