#include "DatasetInProjectWithFileName.h"

DatasetInProjectWithFileName::DatasetInProjectWithFileName(Project* p,
							   int id,
							   const QString& n,
							   const QString& d,
							   const QString& fn,
							   const bool isInProject)
  : DatasetInProject(p,
		     id,
		     n,
		     d,
		     isInProject),
    _fileName(fn)
{}
