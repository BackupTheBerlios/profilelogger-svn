#include "TextNotEmptyCheckConstraint.h"

TextNotEmptyCheckConstraint::TextNotEmptyCheckConstraint(Table* t, const QString& n)
  : CheckConstraint(t, n)
{}

TextNotEmptyCheckConstraint::~TextNotEmptyCheckConstraint()
{}
