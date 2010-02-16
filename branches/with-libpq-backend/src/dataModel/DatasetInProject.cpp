#include "DatasetInProject.h"

DatasetInProject::DatasetInProject(Project* p,
				   const int id,
				   const QString& name,
				   const QString& description,
				   const bool isInProject)
  : Dataset(id, 
	    name, 
	    description,
	    isInProject),
    _project(p)
{}
