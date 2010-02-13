#include "Sequence.h"

Sequence::Sequence(Schema* s, const QString& n)
  : DbInterfacePartInSchema(s, n) 
{
}

Sequence::~Sequence()
{
}

