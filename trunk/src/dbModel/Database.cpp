#include "Database.h"

#include <QCoreApplication>
#include <QStringList>

#include "Schema.h"

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
