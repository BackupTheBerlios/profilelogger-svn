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

  void setDefaultText(const QString& txt) {
    _hasDefaultText = true;
    _defaultText = txt;
  }

  void setDefaultInt(int i) {
    _hasDefaultInt = true;
    _defaultInt = i;
  }

  void setDefaultDouble(double d) {
    _hasDefaultDouble = true;
    _defaultDouble = d;
  }

  bool getHasDefaultText() const {
    return _hasDefaultText;
  }

  bool getHasDefaultInt() const {
    return _hasDefaultInt;
  }

  bool getHasDefaultDouble() const {
    return _hasDefaultDouble;
  }

  QString getDefaultText() const {
    return _defaultText;
  }

  int getDefaultInt() const {
    return _defaultInt;
  }

  double getDefaultDouble() const {
    return _defaultDouble;
  }

  Database::Constants getDefaultConstant() const {
    return _defaultConstant;
  }

 private:
  Database::DataTypes _dataType;
  Sequence* _sequence;
  bool _hasDefaultText;
  QString _defaultText;
  bool _hasDefaultInt;
  int _defaultInt;
  bool _hasDefaultDouble;
  double _defaultDouble;
  Database::Constants _defaultConstant;
};

#endif
