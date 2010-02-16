#ifndef DATASETINPROJECT_H
#define DATASETINPROJECT_H

#include "Dataset.h"

class Project;

class DatasetInProject: public Dataset {
 public:
  DatasetInProject(Project* p,
		   const int id,
		   const QString& name,
		   const QString& description,
		   const bool isInProject);

  virtual ~DatasetInProject() {}

  const bool hasProject() const {
    return 0 != _project;
  }

  void setProject(Project* p) {
    _project = p;
  }

  Project* getProject() const {
    return _project;
  }

 private:
  Project* _project;
};

#endif
