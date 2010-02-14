#ifndef PROJECTMANAGER_H
#define PROJECTMANAGER_H

#include "DataManager.h"

class Project;

class ProjectManager: public DataManager {
  Q_OBJECT
    public:
  ProjectManager(QObject* p, Postgres* pg, ProfileLoggerDatabase* dm);
  virtual ~ProjectManager() {}

  QList<TableColumn*> getInsertColumns() const;
  QList<TableColumn*> getUpdateColumns() const;
  QList<TableColumn*> getSelectColumns() const;
  QList<TableColumn*> getGroupByColumns() const;
  QList<TableColumn*> getOrderByColumns() const;

  QStringList getInsertPlaceholders() const;
  QStringList getUpdatePlaceholders() const;
  QStringList getDeletePlaceholders() const;

  QVariantList getInsertValues(Project* p) const;
  QVariantList getUpdateValues(Project* p) const;
  QVariantList getDeleteValues(Project* p) const;

  virtual void save(Project* p);
  QList<Project*> loadProjects();

 protected:
  virtual void insert(Project* p);
  virtual void update(Project* p);
};

#endif
