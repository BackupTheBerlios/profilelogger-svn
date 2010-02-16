#include "LithologyManager.h"

#include <QDebug>

#include "Lithology.h"
#include "Postgres.h"
#include "SqlFactory.h"
#include "ProfileLoggerDatabase.h"
#include "Project.h"

LithologyManager::LithologyManager(QObject* p, Postgres* pg, ProfileLoggerDatabase* dm)
  : DataManager(p, pg, dm)
{
  setTable(dm->getTable("data.lithologies"));
}

QList<TableColumn*> LithologyManager::getInsertColumns() const
{
  QList<TableColumn*> ret;
  ret << getTable()->getTableColumn("id")
      << getTable()->getTableColumn("name")
      << getTable()->getTableColumn("description")
      << getTable()->getTableColumn("file_name")
      << getTable()->getTableColumn("project_id");
  return ret;
}

QStringList LithologyManager::getInsertPlaceholders() const {
  QStringList ret;
  int i = 1;
  ret << makePlaceholder(i++, getTable()->getTableColumn("id"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("name"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("description"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("file_name"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("project_id"));
  return ret;
}

QVariantList LithologyManager::getInsertValues(Lithology* p) const {
  QVariantList ret;
  p->setId(getPostgres()->nextval(getTable()->getIdColumn()->getSequence()));

  Q_ASSERT(p->hasProject());

  ret << p->getId()
      << p->getName()
      << p->getDescription()
      << p->getFileName()
      << p->getProject()->getId();

  return ret;
}

QList<TableColumn*> LithologyManager::getUpdateColumns() const
{
  QList<TableColumn*> ret;
  ret << getTable()->getTableColumn("name")
      << getTable()->getTableColumn("description")
      << getTable()->getTableColumn("file_name")
      << getTable()->getTableColumn("project_id");
  return ret;
}

QStringList LithologyManager::getUpdatePlaceholders() const {
  QStringList ret;
  int i = 1;
  ret << makePlaceholder(i++, getTable()->getTableColumn("name"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("description"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("file_name"));
  ret << makePlaceholder(i++, getTable()->getTableColumn("project_id"));
  return ret;
}

QVariantList LithologyManager::getUpdateValues(Lithology* p) const {
  Q_ASSERT(p->hasProject());

  QVariantList ret;
  ret << p->getName()
      << p->getDescription()
      << p->getFileName()
      << p->getProject()->getId();
  return ret;
}

QVariantList LithologyManager::getDeleteValues(Lithology* p) const {
  QVariantList ret;
  ret << p->getId();
  return ret;
}

QList<TableColumn*> LithologyManager::getSelectColumns() const
{
  QList<TableColumn*> ret;
  ret << getTable()->getTableColumn("id")
      << getTable()->getTableColumn("name")
      << getTable()->getTableColumn("description")
      << getTable()->getTableColumn("file_name")
      << getTable()->getTableColumn("project_id");
  return ret;
}

QList<Lithology*> LithologyManager::loadLithologies(Project* p) {
  QList<Lithology*> ret;
  
  QList< QMap<QString, QVariant> > d = loadDataWithCursor("load_all_lithologies",
							  getSelectColumns(),
							  getTable(),
							  getOrderByColumns(),
							  getTable()->getTableColumn("project_id"),
							  p->getId());

  for (QList< QMap<QString, QVariant> >::iterator it = d.begin(); it != d.end(); it++) {
    QMap<QString, QVariant> row = *it;
    Q_ASSERT(p);
    ret << new Lithology(p,
			 row["id"].toInt(),
			 row["name"].toString(),
			 row["description"].toString(),
			 row["file_name"].toString(),
			 true);
  }

  return ret;
}

QList<TableColumn*> LithologyManager::getGroupByColumns() const
{
  return QList<TableColumn*>();
}

QList<TableColumn*> LithologyManager::getOrderByColumns() const
{
  QList<TableColumn*> ret;
  ret << getTable()->getTableColumn("name");
  return ret;
}

void LithologyManager::insert(Lithology* p) {
  performInsert(getTable(), 
		getInsertColumns(), 
		getInsertPlaceholders(),
		getInsertValues(p));
}

void LithologyManager::update(Lithology* p) {
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

void LithologyManager::save(Lithology* p) {
  if (p->isInDatabase()) {
    update(p);
  } else {
    insert(p);
  }
}

