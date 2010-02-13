#ifndef DATABASE_H
#define DATABASE_H

#include "DbInterfacePart.h"

#include <QList>

class Schema;
class Table;
class Sequence;

class Database: public DbInterfacePart {
  Q_OBJECT
    public:
  enum Constants {
    NOTHING,
    CURRENT_DATE,
    CURRENT_TIMESTAMP,
    CURRENT_USER
  };

  enum DataTypes {
    DataTypeUnknown,
    DataTypeInt,
    DataTypeText,
    DataTypeDouble,
    DataTypeBool
  };

  Database(QCoreApplication* p, const QString& name);
  virtual ~Database();
  
  Schema* createSchema(const QString& name);
  QList<Schema*>::iterator getFirstSchema();
  QList<Schema*>::iterator getLastSchema();

  Schema* getSchema(const QString& n);
  Sequence* getSequence(const QString& qualifiedName);
  Table* getTable(const QString& qualifiedName);
  
 private:
  QList<Schema*> _schemas;
};

#endif
