#ifndef DBPROJECT_H
#define DBPROJECT_H

#include "DbStandardDataset.h"

class DbProject: public DbStandardDataset {
  Q_DECLARE_TR_FUNCTIONS(DbProject);

 public:
  DbProject(const int id = 0,
	    const QString& name = tr("New Project"),
	    const QString& description = QString::null);
  virtual ~DbProject() {}

  virtual void refresh();
  virtual void remove();

 protected:
  virtual void insert();
  virtual void update();
};

#endif
