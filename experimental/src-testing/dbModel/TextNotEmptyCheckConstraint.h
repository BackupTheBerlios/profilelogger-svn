#ifndef TEXT_NOT_EMPTY_CHECK_CONSTRAINT_H
#define TEXT_NOT_EMPTY_CHECK_CONSTRAINT_H

#include "CheckConstraint.h"

class TextNotEmptyCheckConstraint: public CheckConstraint
{
  Q_OBJECT
    public:
  TextNotEmptyCheckConstraint(Table* t, const QString& name);
  virtual ~TextNotEmptyCheckConstraint();
};

#endif
