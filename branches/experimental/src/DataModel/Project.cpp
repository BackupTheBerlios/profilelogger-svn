#include "Project.h"

Project::Project(Dataset* parent,
		 const int id,
		 const QString& name,
		 const QString& description)
    : StandardDataset(parent,
		      id,
		      name,
		      description)
{
}

Project::~Project()
{
}
