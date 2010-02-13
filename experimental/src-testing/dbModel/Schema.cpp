#include "Schema.h"

#include "Database.h"
#include "Sequence.h"
#include "Table.h"

Schema::Schema(Database* db, const QString& name)
  : DbInterfacePart(db, name)
{}

Schema::~Schema()
{}

Sequence* Schema::createSequence(const QString& name)
{
  _sequences.append(new Sequence(this, name));
  return _sequences.last();
}

QList<Sequence*>::iterator Schema::getFirstSequence() 
{
  return _sequences.begin();
}

QList<Sequence*>::iterator Schema::getLastSequence()
{
  return _sequences.end();
}

Table* Schema::createTable(const QString& name)
{
  _tables.append(new Table(this, name));
  return _tables.last();
}

QList<Table*>::iterator Schema::getFirstTable() 
{
  return _tables.begin();
}

QList<Table*>::iterator Schema::getLastTable()
{
  return _tables.end();
}
