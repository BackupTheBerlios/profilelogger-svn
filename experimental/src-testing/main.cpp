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

void crebas(Postgres* pg, AppDatabase* db) {
  SqlFactory f(0);
  QStringList sql;

  sql << "DROP SCHEMA data CASCADE";

  for (QList<Schema*>::iterator it = db->getFirstSchema(); it != db->getLastSchema(); it++) {
    Schema* schema = *it;

    QStringList buf = f.make(schema);
    sql << buf;

    for (QList<Sequence*>::iterator seqIt = schema->getFirstSequence(); seqIt != schema->getLastSequence(); seqIt++) {
      sql << f.make(*seqIt);
    }
  }

  for (QList<Schema*>::iterator sit = db->getFirstSchema(); sit != db->getLastSchema(); sit++) {
    Schema* schema = *sit;

    for (QList<Table*>::iterator tit = schema->getFirstTable(); tit != schema->getLastTable(); tit++) {
      Table* table = *tit;
      sql << f.make(table);

      for (QList<UniqueConstraint*>::iterator ucit = table->getFirstUniqueConstraint(); ucit != table->getLastUniqueConstraint(); ucit++) {
        sql << f.make(*ucit);
      }
      for (QList<TextNotEmptyCheckConstraint*>::iterator cit = table->getFirstTextNotEmptyCheckConstraint(); cit != table->getLastTextNotEmptyCheckConstraint(); cit++
	   ) {
        sql << f.make(*cit);
      }
      if (table->hasPrimaryKey()) {
        sql << f.make(table->getPrimaryKey());
      }
    }
  }

  for (QList<Schema*>::iterator sit = db->getFirstSchema(); sit != db->getLastSchema(); sit++) {
    Schema* schema = *sit;

    for (QList<Table*>::iterator tit = schema->getFirstTable(); tit != schema->getLastTable(); tit++) {
      Table* table = *tit;

      for (QList<ForeignKey*>::iterator fkit = table->getFirstForeignKey(); fkit != table->getLastForeignKey(); fkit++) {
        sql << f.make(*fkit);
      }

      for(QList<TableColumn*>::iterator cit = table->getFirstTableColumn(); cit != table->getLastTableColumn(); cit++) {
        TableColumn* c = *cit;

        if (c->hasSequence()) {
          sql << f.makeDefaultFromSequence(c);
        }
        if (c->getHasDefaultText()) {
          sql << f.makeDefaultText(c);
        }
        if (c->getHasDefaultInt()) {
          sql << f.makeDefaultInt(c);
        }
        if (c->getHasDefaultDouble()) {
          sql << f.makeDefaultDouble(c);
        }
        if (c->getDefaultConstant() != Database::NOTHING) {
          sql << f.makeDefaultFromConstant(c);
        }
      }
    }
  }

  for (QStringList::iterator it = sql.begin(); it != sql.end(); it++) {
    pg->exec(*it);
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
    crebas(&pg, &db);
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
