#ifndef DATABASE_H
#define DATABASE_H

#include "DbInterfacePart.h"

#include <QList>

class Schema;

class Database: public DbInterfacePart {
  Q_OBJECT
    public:
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
 private:
  QList<Schema*> _schemas;
};

#endif
