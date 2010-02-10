#include "ProfileInCorrelation.h"

ProfileInCorrelation::ProfileInCorrelation(int id,
					   const QString& name,
					   const QString& description,
					   Profile* profile,
					   int position)
  : Dataset(id,
	    name,
	    description),
    _profile(profile),
    _position(position) 
{
}

ProfileInCorrelation::~ProfileInCorrelation()
{}
