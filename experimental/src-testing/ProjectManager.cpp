#include "ProjectManager.h"

#include <QDebug>

#include "Project.h"
#include "Postgres.h"
#include "SqlFactory.h"
#include "AppDatabase.h"

ProjectManager::ProjectManager(QObject* p, Postgres* pg, AppDatabase* dm)
  : DataManager(p, pg, dm)
{
  setTable(dm->getTable("data.projects"));
}

QVariantList ProjectManager::getInsertValues(Project* p) const {
  QVariantList ret;
  p->setId(getPostgres()->nextval(getTable()->getIdColumn()->getSequence()));

  ret << p->getId()
      << p->getName()
      << p->getDescription();

  return ret;
}

QVariantList ProjectManager::getUpdateValues(Project* p) const {
  QVariantList ret;
  ret << p->getName()
      << p->getDescription();
  return ret;
}

QVariantList ProjectManager::getDeleteValues(Project* p) const {
  QVariantList ret;
  ret << p->getId();
  return ret;
}

QStringList ProjectManager::getInsertPlaceholders() const {
  QStringList ret;
  int i = 1;
  ret << makePlaceholder(i++, getTable()->getTableColumn("id"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("name"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("description"));
  return ret;
}

QStringList ProjectManager::getUpdatePlaceholders() const {
  QStringList ret;
  int i = 1;
  ret << makePlaceholder(i++, getTable()->getTableColumn("name"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("description"));  
  return ret;
}


QList<TableColumn*> ProjectManager::getInsertColumns() const
{
  QList<TableColumn*> ret;
  ret << getTable()->getTableColumn("id")
      << getTable()->getTableColumn("name")
      << getTable()->getTableColumn("description");
  return ret;
}

QList<TableColumn*> ProjectManager::getUpdateColumns() const
{
  QList<TableColumn*> ret;
  ret << getTable()->getTableColumn("name")
      << getTable()->getTableColumn("description");
  return ret;
}

QList<TableColumn*> ProjectManager::getSelectColumns() const
{
  QList<TableColumn*> ret;
  ret << getTable()->getTableColumn("id")
      << getTable()->getTableColumn("name")
      << getTable()->getTableColumn("description");
  return ret;
}

QList<TableColumn*> ProjectManager::getGroupByColumns() const
{
  return QList<TableColumn*>();
}

QList<TableColumn*> ProjectManager::getOrderByColumns() const
{
  QList<TableColumn*> ret;
  ret << getTable()->getTableColumn("name");
  return ret;
}

void ProjectManager::insert(Project* p) {
  performInsert(getTable(), 
		getInsertColumns(), 
		getInsertPlaceholders(),
		getInsertValues(p));
}

void ProjectManager::update(Project* p) {
  TableColumn* idCol = getTable()->getIdColumn();
  QVariantList values = getUpdateValues(p);

  performUpdate(getTable(),
		getUpdateColumns(),
		getUpdatePlaceholders(),
		values,
		idCol,
		makePlaceholder(values.size() + 1, idCol),
		p->getId());
}

void ProjectManager::save(Project* p) {
  if (p->hasId()) {
    update(p);
  } else {
    insert(p);
  }
}


QList<Project*> ProjectManager::loadProjects() {
  QList<Project*> ret;
  getPostgres()->declareSelectCursor("projects", 
				     getSelectColumns(),
				     getTable(),
				     getOrderByColumns());

  PGresult* res = getPostgres()->fetchAllInCursor("projects");

  QList< QMap<QString, QVariant> > d = getPostgres()->getData(res);

  for (QList< QMap<QString, QVariant> >::iterator it = d.begin(); it != d.end(); it++) {
    QMap<QString, QVariant> row = *it;

    ret << new Project(row["id"].toInt(),
		       row["name"].toString(),
		       row["description"].toString());
  }

  getPostgres()->closeCursor("projects");
  getPostgres()->clearResult(res);
  return ret;
}
