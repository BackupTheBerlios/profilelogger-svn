#include "StandardDataset.h"

StandardDataset::StandardDataset(Dataset* parent,
				 const int id,
				 const QString& name,
				 const QString& description)
    : Dataset(parent,
	      id),
      _name(name),
      _description(description)
{
}

StandardDataset::~StandardDataset()
{
}

void StandardDataset::setName(const QString& n) 
{
    _name = n;
}

void StandardDataset::setDescription(const QString& d)
{
    _description = d;
}


QString StandardDataset::getName() const 
{    
    return _name;
}

QString StandardDataset::getDescription() const
{
    return _description;
}

