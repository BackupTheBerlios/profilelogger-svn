#include "TableColumn.h"

TableColumn::TableColumn(Table* t, const QString& name, Database::DataTypes dt)
  : DbInterfacePartInTable(t, name),
    _dataType(dt),
    _sequence(0),
    _hasDefaultText(false),
    _hasDefaultInt(false),
    _hasDefaultDouble(false),
    _defaultConstant(Database::NOTHING)
{}

TableColumn::~TableColumn()
{}
