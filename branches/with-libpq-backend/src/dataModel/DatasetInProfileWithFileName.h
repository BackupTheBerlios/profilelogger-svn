#ifndef DATASETINPROFILEWITHFILENAME_H
#define DATASETINPROFILEWITHFILENAME_H

#include "DatasetInProfile.h"

class DatasetInProfileWithFileName: public DatasetInProfile {
 public:
  DatasetInProfileWithFileName(Profile* p,
			       int id,
			       const QString& name,
			       const QString& description,
			       const QString& fileName,
			       const bool isInDatabase);

  virtual ~DatasetInProfileWithFileName() {}

  const bool hasFileName() const {
    return !_fileName.isEmpty();
  }

  void setFileName(const QString& n) {
    _fileName = n;
  }

  QString getFileName() const {
    return _fileName;
  }

 private:
  QString _fileName;
};

#endif
