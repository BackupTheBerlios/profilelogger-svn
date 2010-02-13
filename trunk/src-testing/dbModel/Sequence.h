#ifndef SEQUENCE_H
#define SEQUENCE_H

#include "DbInterfacePartInSchema.h"

class Sequence: public DbInterfacePartInSchema {
  Q_OBJECT
    public:
  Sequence(Schema* s, const QString& name);
  virtual ~Sequence();
};

#endif
