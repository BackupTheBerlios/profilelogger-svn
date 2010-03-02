#include "Dataset.h"

Dataset::Dataset(QObject* parent,
		 const int id)
    : QObject(parent),
      _id(id)
{
}

Dataset::~Dataset()
{
}

int Dataset::getId() const
{
    return _id;
}

void Dataset::setId(const int id)
{	
    _id = id;
}
    
