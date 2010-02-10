#include "TableColumn.h"

TableColumn::TableColumn(Table* t, const QString& name, Database::DataTypes dt)
  : DbInterfacePartInTable(t, name),
    _dataType(dt),
    _sequence(0)
{}

TableColumn::~TableColumn()
{}
