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

QList<QVariant> ProjectManager::getInsertValues(Project* p) const {
  QList<QVariant> ret;
  p->setId(getPostgres()->nextval(getTable()->getIdColumn()->getSequence()));

  ret << p->getId()
      << p->getName()
      << p->getDescription();
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

QStringList ProjectManager::getInsertColumns() const
{
  QStringList ret;
  ret << getTable()->getTableColumn("id")->getName()
      << getTable()->getTableColumn("name")->getName()
      << getTable()->getTableColumn("description")->getName();
  return ret;
}

QStringList ProjectManager::getUpdateColumns() const
{
  QStringList ret;
  ret << getTable()->getTableColumn("name")->getName()
      << getTable()->getTableColumn("description")->getName();
  return ret;
}

QStringList ProjectManager::getSelectColumns() const
{
  QStringList ret;
  ret << getTable()->getTableColumn("id")->getName()
      << getTable()->getTableColumn("name")->getName()
      << getTable()->getTableColumn("description")->getName();
  return ret;
}

QStringList ProjectManager::getGroupByColumns() const
{
  QStringList ret;
  return ret;
}

QStringList ProjectManager::getOrderByColumns() const
{
  QStringList ret;
  ret << getTable()->getTableColumn("name")->getName();
  return ret;
}

void ProjectManager::insert(Project* p) {
  qDebug() << "ProjectManager::insert(...) " << p->toString();

  QStringList placeholders = getInsertPlaceholders();

  QString sql = QString("INSERT INTO %1(%2) VALUES(%3)")
    .arg(getTable()->getQualifiedName())
    .arg(getInsertColumns().join(", "))
    .arg(placeholders.join(", "));

  qDebug() << "sql: " << sql;

  char* paramValues[3];
  p->setId(getPostgres()->nextval(getTable()->getIdColumn()->getSequence()));
  paramValues[0] = QString(p->getId()).toUtf8().data();
paramValues[1] = QString(p->getName().data()).toUtf8().data();
  paramValues[2] = QString(p->getDescription().data()).toUtf8().data();

  qDebug() << "$1: " << paramValues[0] << " " << p->getId() << "\n"
	   << "$2: " << paramValues[1] << " " << p->getName() << "\n"
	   << "$3: " << paramValues[2] << " " << p->getDescription();

  PGresult* res = getPostgres()->execParams(sql, 3, paramValues);
  ExecStatusType t = PQresultStatus(res);

  qDebug() << "!PQresStatus: " << PQresStatus(t)
	   << "!PQresultErrorMessage: " << PQresultErrorMessage(res)
	   << "!PG_DIAG_MESSAGE_DETAIL: " << PQresultErrorField(res, PG_DIAG_MESSAGE_DETAIL)
	   << "!PG_DIAG_MESSAGE_HINT: " << PQresultErrorField(res, PG_DIAG_MESSAGE_HINT);

  if (PGRES_COMMAND_OK != PQresultStatus(res)) {
    throw DatabaseError(tr("Could not insert project '%1'.").arg(p->toString()),
			sql,
			PQresultErrorMessage(res));
  }
}

void ProjectManager::update(Project* p) {
  QStringList kv;
  QStringList placeholders;
  QStringList cols = getUpdateColumns();
  placeholders << QString("$1::%1").arg(getSqlFactory()->typeToString(getTable()->getTableColumn("name")->getDataType()))
	       << QString("$2::%1").arg(getSqlFactory()->typeToString(getTable()->getTableColumn("description")->getDataType()));

  for (int i = 0; i < placeholders.size(); i++) {
    kv << QString("%1 = %2").arg(cols.at(i)).arg(placeholders.at(i));
  }

  QString sql = QString("UPDATE %1 SET %2 WHERE %3 = $%4::%5")
    .arg(getTable()->getQualifiedName())
    .arg(kv.join(", "))
    .arg(getTable()->getIdColumn()->getName())
    .arg(kv.size() + 1)
    .arg(getSqlFactory()->typeToString(getTable()->getIdColumn()->getDataType()));

  char* params[3];
  params[0] = p->getName().toUtf8().data();
  params[1] = p->getDescription().toUtf8().data();
  params[2] = QString(p->getId()).toUtf8().data();

  PGresult* res = getPostgres()->execParams(sql, 3, params);
  
  if (PGRES_COMMAND_OK != PQresultStatus(res)) {
    throw DatabaseError(tr("Could not update project '%1'.").arg(p->toString()),
			sql,
			PQresultErrorMessage(res));
  }
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
  getPostgres()->declareCursor("projects", 
			       QString("SELECT %1 from %2 order by %3")
			       .arg(getSelectColumns().join(", "))
			       .arg(getTable()->getQualifiedName())
			       .arg(getOrderByColumns().join(", ")));

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
