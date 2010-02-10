#ifndef PRIMARY_KEY_H
#define PRIMARY_KEY_H

#include "TableConstraint.h"

class PrimaryKey: public TableConstraint
{
  Q_OBJECT
    public:
  PrimaryKey(Table* t, const QString& name);
  virtual ~PrimaryKey();
};

#endif
