#ifndef LITHOLOGYMANAGER_H
#define LITHOLOGYMANAGER_H

#include "DataManager.h"

class Lithology;
class Project;

class LithologyManager: public DataManager {
  Q_OBJECT
    public:
  LithologyManager(QObject* p, Postgres* pg, ProfileLoggerDatabase* dm);
  virtual ~LithologyManager() {}

  QList<TableColumn*> getInsertColumns() const;
  QList<TableColumn*> getUpdateColumns() const;
  QList<TableColumn*> getSelectColumns() const;
  QList<TableColumn*> getGroupByColumns() const;
  QList<TableColumn*> getOrderByColumns() const;

  QStringList getInsertPlaceholders() const;
  QStringList getUpdatePlaceholders() const;
  QStringList getDeletePlaceholders() const;

  QVariantList getInsertValues(Lithology* p) const;
  QVariantList getUpdateValues(Lithology* p) const;
  QVariantList getDeleteValues(Lithology* p) const;

  virtual void save(Lithology* p);
  QList<Lithology*> loadLithologies(Project* p);

 protected:
  virtual void insert(Lithology* p);
  virtual void update(Lithology* p);
};

#endif
