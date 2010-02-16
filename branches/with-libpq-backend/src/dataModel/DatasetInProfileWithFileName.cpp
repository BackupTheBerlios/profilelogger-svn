#include "DatasetInProfileWithFileName.h"

DatasetInProfileWithFileName::DatasetInProfileWithFileName(Profile* p,
							   int id,
							   const QString& n,
							   const QString& d,
							   const QString& fn,
							   const bool isInDatabase)
  : DatasetInProfile(p,
		     id,
		     n,
		     d,
		     isInDatabase),
    _fileName(fn)
{}
