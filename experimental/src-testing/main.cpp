#include <QApplication>
#include <QCoreApplication>

#include <QDebug>

#include "Postgres.h"

#include "DatabaseError.h"
#include "AppDatabase.h"
#include "SqlFactory.h"
#include "ProjectManager.h"

#include "Database.h"
#include "Schema.h"
#include "Sequence.h"
#include "Table.h"
#include "TableColumn.h"
#include "UniqueConstraint.h"
#include "PrimaryKey.h"
#include "TextNotEmptyCheckConstraint.h"

#include "Dataset.h"
#include "Project.h"

void printData(QList< QMap<QString, QVariant> > d) {
  for (QList< QMap<QString, QVariant> >::iterator r = d.begin(); r != d.end(); r++) {
    QStringList row;
    for (QMap<QString, QVariant>::iterator c = (*r).begin(); c != (*r).end(); c++) {
      row << c.value().toString();
    }
    qDebug() << row.join("\t");
  }
}

void testCursor(Postgres* pg) {
  pg->declareCursor("databases", "select * from pg_database");
  PGresult* res = pg->fetchAllInCursor("databases");
  printData(pg->getData(res));
  pg->closeCursor("databases");
  pg->clearResult(res);
}

void testExecDDL(Postgres* pg) {
  pg->exec("CREATE SCHEMA foo");
  pg->exec("DROP SCHEMA foo");
}

void loadProjects(ProjectManager* m) {
  QList<Project*> pl = m->loadProjects();

  qDebug() << "--- Loading Projects ---";
  for (QList<Project*>::iterator it = pl.begin(); it != pl.end(); it++) {
    qDebug() << (*it)->toString();
  }
  qDebug() << "--- End Of Projects ---";
}

void testProjectModel(ProjectManager* m) {
  Project p1;
  Project p2;
  Project p3;

  p1.setName("Project A");
  p1.setDescription("Description for project a");

  p2.setName("foo");
  p3.setName("modify me");

  m->save(&p1);
  m->save(&p2);
  m->save(&p3);

  loadProjects(m);

  QList<Project*> projects = m->loadProjects();
  int i = 0;
  for (QList<Project*>::iterator it = projects.begin(); it != projects.end(); it++) {
    (*it)->setDescription(QString("Description #%1").arg(i++));
  }

  loadProjects(m);

  for (QList<Project*>::iterator it = projects.begin(); it != projects.end(); it++) {
    m->save(*it);
  }

  loadProjects(m);

  projects.at(2)->setName("changed!");
  m->save(projects.at(2));
  loadProjects(m);
  m->remove(projects.at(2));

  loadProjects(m);
}

int main(int argc, char** argv) {
  QApplication a(argc, argv);
  AppDatabase db(&a);
  Postgres pg(0);
  ProjectManager pm(&a, &pg, &db);

  try {
    pg.connect();
    pg.begin();
    pg.createSchema(&db);
    pg.commit();

    pg.begin();
    testProjectModel(&pm);
    pg.commit();

    pg.begin();
    loadProjects(&pm);
    testCursor(&pg);
    pg.commit();

    pg.close();
  } catch(DatabaseError e) {
    qDebug() << e.text();
    pg.rollback();
    pg.close();
    exit(1);
  }

  //  return a.exec();
  return 0;
}
