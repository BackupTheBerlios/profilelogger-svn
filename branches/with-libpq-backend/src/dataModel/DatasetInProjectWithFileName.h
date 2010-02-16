#ifndef DATASETINPROJECTWITHFILENAME_H
#define DATASETINPROJECTWITHFILENAME_H

#include "DatasetInProject.h"

class DatasetInProjectWithFileName: public DatasetInProject {
 public:
  DatasetInProjectWithFileName(Project* p,
			       int id,
			       const QString& name,
			       const QString& description,
			       const QString& fileName,
			       const bool isInDatabase);
  virtual ~DatasetInProjectWithFileName() {}

  bool hasFileName() const {
    return 0 != _fileName;
  }

  void setFileName(const QString& s) {
    _fileName = s;
  }

  QString getFileName() const {
    return _fileName;
  }

 private:
  QString _fileName;
};

#endif
