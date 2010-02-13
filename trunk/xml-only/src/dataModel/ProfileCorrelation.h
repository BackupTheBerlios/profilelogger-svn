#ifndef PROFILE_CORRELATION_H
#define PROFILE_CORRELATION_H

#include "Dataset.h"

#include <QObject>
#include <QList>

class BedCorrelation;
class ProfileInCorrelation;
class Profile;

class ProfileCorrelation: public Dataset {
 public:
  ProfileCorrelation(int id = 0,
		     const QString& name = QObject::tr("Profile Correlation"),
		     const QString& description = QString::null);
  virtual ~ProfileCorrelation();

  BedCorrelation* createBedCorrelation(int id = 0);
  BedCorrelation* getBedCorrelation(int id);
  void deleteBedCorrelation(BedCorrelation* c);
  int getBedCorrelationCount();
  QList<BedCorrelation*>::iterator getFirstBedCorrelation();
  QList<BedCorrelation*>::iterator getLastBedCorrelation();
  
  ProfileInCorrelation* addProfile(Profile* p, int id = 0, int position = -1);
  ProfileInCorrelation* getById(int id);
  void remove(ProfileInCorrelation* profile);
  QList<ProfileInCorrelation*>::iterator getFirstProfileInCorrelation();
  QList<ProfileInCorrelation*>::iterator getLastProfileInCorrelation();
  int getProfileInCorrelationCount();

 private:
  void renumberProfilesInBed();
  int _lastBedCorrelationId;
  int _lastProfileInCorrelationId;

  QList<BedCorrelation*> _bedCorrelations;
  QList<ProfileInCorrelation*> _profiles;
};

#endif
