#ifndef UNIQUE_CONSTRAINT_H
#define UNIQUE_CONSTRAINT_H

#include "TableConstraint.h"

class UniqueConstraint: public TableConstraint
{
  Q_OBJECT
    public:
  UniqueConstraint(Table* t, const QString& name);
  virtual ~UniqueConstraint();
};

#endif
