#include "ProfileCorrelation.h"

#include "BedCorrelation.h"
#include "ProfileInCorrelation.h"
#include "Profile.h"

ProfileCorrelation::ProfileCorrelation(int id,
				       const QString& name,
				       const QString& description)
  : Dataset(id,
	    name,
	    description),
    _lastBedCorrelationId(0),
    _lastProfileInCorrelationId(0)
{}

ProfileCorrelation::~ProfileCorrelation(){}

BedCorrelation* ProfileCorrelation::createBedCorrelation(int id) {
  if (id != 0) {
    if (id > _lastBedCorrelationId) {
      _lastBedCorrelationId = id;
    }
  } else {
    _lastBedCorrelationId++;
  }

  _bedCorrelations.append(new BedCorrelation(_lastBedCorrelationId, 0, 0));
  return getBedCorrelation(_lastBedCorrelationId);
}

BedCorrelation* ProfileCorrelation::getBedCorrelation(int id) {
  for (int i = 0; i < _bedCorrelations.size(); i++) {
    BedCorrelation* c = _bedCorrelations.at(i);

    if (c->getId() == id) {
      return c;
    }
  }

  return 0;
}

void ProfileCorrelation::deleteBedCorrelation(BedCorrelation* c) {
  if (!c) {
    return;
  }

  int i = _bedCorrelations.indexOf(c);

  if (-1 == i) {
    return;
  }

  BedCorrelation* cc = _bedCorrelations.takeAt(i);

  if (cc) {
    delete cc;
  }
}
 
int ProfileCorrelation::getBedCorrelationCount() {
  return _bedCorrelations.size();
}

QList<BedCorrelation*>::iterator ProfileCorrelation::getFirstBedCorrelation() {
  return _bedCorrelations.begin();
}

QList<BedCorrelation*>::iterator ProfileCorrelation::getLastBedCorrelation() {
  return _bedCorrelations.end();
}

ProfileInCorrelation* ProfileCorrelation::addProfile(Profile* p, int id, int position) {
  if (!p) {
    return 0;
  }

  if (id > 0) {
    if (id > _lastProfileInCorrelationId) {
      _lastProfileInCorrelationId = id;
    }
  } else {
    _lastProfileInCorrelationId++;
  }
  
  if (position > 0) {
    _profiles.insert(position, new ProfileInCorrelation(_lastProfileInCorrelationId,
							p->getName(),
							p->getDescription(),
							p,
							position));
  } else {
    _profiles.append(new ProfileInCorrelation(_lastProfileInCorrelationId,
					      p->getName(),
					      p->getDescription(),
					      p));
  }
  renumberProfilesInBed();
  return getById(_lastProfileInCorrelationId);
}

ProfileInCorrelation* ProfileCorrelation::getById(int id) {
  for (QList<ProfileInCorrelation*>::iterator it = _profiles.begin();
       it != _profiles.end();
       it++) {
    ProfileInCorrelation* p = *it;
    if (p) {
      if (p->getId() == id) {
	return p;
      }
    }
  }

  return 0;
}

void ProfileCorrelation::remove(ProfileInCorrelation* profile) {
  int i = _profiles.indexOf(profile);

  if (-1 == i) {
    return;
  }

  ProfileInCorrelation* tmp = _profiles.takeAt(i);

  if (tmp) {
    delete tmp;
  }
}

QList<ProfileInCorrelation*>::iterator ProfileCorrelation::getFirstProfileInCorrelation() {
  return _profiles.begin();
}

QList<ProfileInCorrelation*>::iterator ProfileCorrelation::getLastProfileInCorrelation() {
  return _profiles.end();
}

int ProfileCorrelation::getProfileInCorrelationCount() {
  return _profiles.size();
}

void ProfileCorrelation::renumberProfilesInBed() {
  for (int i = 0; i < _profiles.size(); i++) {
    ProfileInCorrelation* c = _profiles.at(i);
    c->setPosition(i);
  }
}

