#include "Database.h"

#include <QCoreApplication>
#include <QStringList>

#include "Schema.h"
#include "Table.h"
#include "Sequence.h"

Database::Database(QCoreApplication* p, const QString& n)
  : DbInterfacePart(p, n)
{}

Database::~Database() 
{}

Schema* Database::createSchema(const QString& name) {
  _schemas.append(new Schema(this, name));
  return _schemas.last();
}

QList<Schema*>::iterator Database::getFirstSchema() {
  return _schemas.begin();
}

QList<Schema*>::iterator Database::getLastSchema() {
  return _schemas.end();
}

Schema* Database::getSchema(const QString& n) {
  for(QList<Schema*>::iterator it = getFirstSchema(); it != getLastSchema(); it++) {
    Schema* s = *it;

    if (n == s->getName()) {
      return s;
    }
  }

  return 0;
}

Sequence* Database::getSequence(const QString& n) {
  QStringList components = n.split(".");

  QString sn = components[0];
  QString seqN = components[1];

  Schema* schema = getSchema(sn);

  if (!schema) {
    return 0;
  }
  
  for (QList<Sequence*>::iterator it = schema->getFirstSequence(); it != schema->getLastSequence(); it++) {
    Sequence* seq = *it;

    if (seq->getName() == seqN) {
      return seq;
    }
  }

  return 0;
}

Table* Database::getTable(const QString& n) {
  QStringList components = n.split(".");

  QString sn = components[0];
  QString tN = components[1];

  Schema* schema = getSchema(sn);

  if (!schema) {
    return 0;
  }
  
  for (QList<Table*>::iterator it = schema->getFirstTable(); it != schema->getLastTable(); it++) {
    Table* t = *it;

    if (t->getName() == tN) {
      return t;
    }
  }

  return 0;
}
