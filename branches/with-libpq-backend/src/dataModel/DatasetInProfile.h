#ifndef DATASETINPROFILE_H
#define DATASETINPROFILE_H

#include "Dataset.h"

class Profile;

class DatasetInProfile: public Dataset {
 public:
  DatasetInProfile(Profile* p,
		   const int id,
		   const QString& name,
		   const QString& description,
		   const bool isInDatabase);
  virtual ~DatasetInProfile() {}

  bool hasProfile() const {
    return 0 != _profile;
  }

  void setProfile(Profile* p) {
    _profile = p;
  }

  Profile* getProfile() const {
    return _profile;
  }

 private:
  Profile* _profile;
};

#endif
