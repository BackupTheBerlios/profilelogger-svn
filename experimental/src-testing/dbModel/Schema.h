#ifndef SCHEMA_H
#define SCHEMA_H

#include "DbInterfacePart.h"

class Database;

#include <QList>

class Sequence;
class Table;

class Schema: public DbInterfacePart {
Q_OBJECT
  public:
  Schema(Database* db, const QString& name);
  virtual ~Schema(); 

  Sequence* createSequence(const QString& name);
  QList<Sequence*>::iterator getFirstSequence();
  QList<Sequence*>::iterator getLastSequence();

  Table* createTable(const QString& name);
  QList<Table*>::iterator getFirstTable();
  QList<Table*>::iterator getLastTable();

 private:
  QList<Sequence*> _sequences;
  QList<Table*> _tables;
};

#endif
