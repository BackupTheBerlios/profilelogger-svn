#ifndef PROFILE_IN_CORRELATION_H
#define PROFILE_IN_CORRELATION_H

#include "Dataset.h"

class Profile;

class ProfileInCorrelation: public Dataset {
 public:
  ProfileInCorrelation(int id = 0,
		       const QString& name = tr("Profile In Correlation"),
		       const QString& description = QString::null,
		       Profile* profile = 0,
		       int position = 0);
  virtual ~ProfileInCorrelation();

  const bool hasProfile() const {
    return 0 != _profile;
  }

  void setProfile(Profile* p) {
    _profile = p;
  }

  Profile* getProfile() {
    return _profile;
  }

  void setPosition(int p) {
    _position = p;
  }

  int getPosition() const {
    return _position;
  }

 private:
  Profile* _profile;
  int _position;
};

#endif
