#ifndef CHECK_CONSTRAINT_H
#define CHECK_CONSTRAINT_H

#include "TableConstraint.h"

class CheckConstraint: public TableConstraint
{
  Q_OBJECT
    public:
  CheckConstraint(Table* t, const QString& name);
  virtual ~CheckConstraint();
};

#endif
