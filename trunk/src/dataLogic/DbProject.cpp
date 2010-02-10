#include "DbProject.h"

#include <QSqlQuery>
#include <QSqlRecord>

#include "DatabaseConnection.h"
#include "ProfileLoggerDatabase.h"
#include "SqlFactory.h"

DbProject::DbProject(const int id,
		     const QString& name,
		     const QString& description)
  : DbStandardDataset(id,
		      name,
		      description)
{
  setSequence(getDb()->getProjectsSequence());
  setTable(getDb()->getProjectsTable());
  refresh();
}

void DbProject::refresh() {
  SqlFactory f(getApp());

  Table* t = getTable();
  QList<TableColumn*> cols;
  QStringList fields;
  TableColumn* idCol = t->getIdColumn();

  cols << t->getTableColumn("id")
       << t->getTableColumn("name")
       << t->getTableColumn("description");

  for (int i = 0; i < cols.size(); i++) {
    fields << cols.at(i)->getName();
  }

  QSqlQuery q = getDbConn()->createQuery(f.makeSelectById(t,
							  cols,
							  fields,
							  idCol,
							  getId()));
  getDbConn()->execSelect(&q, 1);
  q.first();

  QSqlRecord r = q.record();

  int idPos = r.indexOf("id");
  int namePos = r.indexOf("name");
  int descriptionPos = r.indexOf("description");
  
  setId(r.value(idPos).toInt());
  setName(r.value(namePos).toString());
  setDescription(r.value(descriptionPos).toString());
  setIsDirty(false);
}

void DbProject::remove() {
  SqlFactory f(getApp());
  
  QSqlQuery q = getDbConn()->createQuery(f.makeDelete(getTable(), ":id"));
  getDbConn()->prepare(&q);
  getDbConn()->bindValue(&q, ":id", getId());
  getDbConn()->execDelete(&q, 1);
}

void DbProject::update() {
  SqlFactory f(getApp());

  Table* t = getTable();
  QList<TableColumn*> cols;
  QStringList placeholders;
  QList<QVariant> values;

  cols << t->getTableColumn("name")
       << t->getTableColumn("description");

  placeholders << ":name"
	       << ":description";

  QSqlQuery q = getDbConn()->createQuery(f.makeUpdate(t,
						      cols,
						      placeholders,
						      ":id"));
  getDbConn()->bindValues(&q, placeholders, values);
  q.bindValue(":id", getId());
  getDbConn()->execUpdate(&q, 1);
  refresh();
}

void DbProject::insert() {
  SqlFactory f(getApp());

  Table* t = getTable();
  QList<TableColumn*> cols;
  QStringList placeholders;
  QList<QVariant> values;

  cols << t->getTableColumn("id")
       << t->getTableColumn("name")
       << t->getTableColumn("description");

  placeholders << ":id"
	       << ":name"
	       << ":description";
  values << getId()
	 << getName()
	 << getDescription();

  QSqlQuery q = getDbConn()->createQuery(f.makeInsert(t,
						      cols,
						      placeholders));
  getDbConn()->bindValues(&q, placeholders, values);
  getDbConn()->execInsert(&q, 1);
  refresh();
}
