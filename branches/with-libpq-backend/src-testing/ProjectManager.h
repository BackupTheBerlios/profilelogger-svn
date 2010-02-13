#ifndef PROJECTMANAGER_H
#define PROJECTMANAGER_H

#include "DataManager.h"

class Project;

class ProjectManager: public DataManager {
  Q_OBJECT
    public:
  ProjectManager(QObject* p, Postgres* pg, AppDatabase* dm);
  virtual ~ProjectManager() {}

  QStringList getInsertColumns() const;
  QStringList getUpdateColumns() const;
  QStringList getSelectColumns() const;
  QStringList getGroupByColumns() const;
  QStringList getOrderByColumns() const;
  QStringList getInsertPlaceholders() const;
  QList<QVariant> getInsertValues(Project* p) const;

  virtual void save(Project* p);
  QList<Project*> loadProjects();

 protected:
  virtual void insert(Project* p);
  virtual void update(Project* p);
};

#endif
