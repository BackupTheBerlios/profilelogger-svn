#include "DbStandardDataset.h"

DbStandardDataset::DbStandardDataset(const int id,
				     const QString& name,
				     const QString& description)
  : DbDataset(id),
    _name(name),
    _description(description)
{
  setName(name);
  setDescription(description);
}

QString DbStandardDataset::toString() const {
  return tr("Name [%1]").arg(getId());
}

