#ifndef PROJECT_H
#define PROJECT_H

#include "Dataset.h"

class Project: public Dataset {
 public:
  Project(int id = 0,
	  const QString& name = QString::null,
	  const QString& description = QString::null);
  virtual QString toString() const {
    return QString("%1 [%2]").arg(getName()).arg(getId());
  }

  void setName(const QString& s) {
    _name = s;
  }

  void setDescription(const QString& s) {
    _description = s;
  }

  QString getName() const {
    return _name;
  }

  QString getDescription() const {
    return _description;
  }

 private:
  QString _name;
  QString _description;
};

#endif
