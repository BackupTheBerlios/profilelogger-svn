#include "DatasetInProfile.h"

DatasetInProfile::DatasetInProfile(Profile* p,
				   int id,
				   const QString& n,
				   const QString& d,
				   const bool isInDatabase)
  : Dataset(id,
	    n,
	    d,
	    isInDatabase),
    _profile(p)
{}

