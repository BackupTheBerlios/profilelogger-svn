#ifndef TABLE_COLUMN_H
#define TABLE_COLUMN_H

#include "DbInterfacePartInTable.h"

#include "Database.h"
#include "Schema.h"
#include "Sequence.h"
#include "Table.h"

class Sequence;

class TableColumn: public DbInterfacePartInTable
{
  Q_OBJECT
    public:
  TableColumn(Table* t, const QString& name, Database::DataTypes dt);
  virtual ~TableColumn();

  Database::DataTypes getDataType() const {
    return _dataType;
  }

  bool hasSequence() const {
    return 0 != _sequence;
  }
  
  void setSequence(Sequence* s) {
    _sequence = s;
  }
  
  Sequence* getSequence() const {
    return _sequence;
  }

  virtual QString getCompleteName();

 private:
  Database::DataTypes _dataType;
  Sequence* _sequence;
};

#endif
