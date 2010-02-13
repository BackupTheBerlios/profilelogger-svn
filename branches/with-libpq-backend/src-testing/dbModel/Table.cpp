#include "Table.h"

#include "Schema.h"
#include "TableColumn.h"
#include "PrimaryKey.h"
#include "UniqueConstraint.h"
#include "TextNotEmptyCheckConstraint.h"
#include "ForeignKey.h"

Table::Table(Schema* s, const QString& name)
  : DbInterfacePartInSchema(s, name),
    _primaryKey(0)
{}

Table::~Table()
{}

TableColumn* Table::createTableColumn(const QString& name, Database::DataTypes t) {
  _columns.append(new TableColumn(this, name, t));
  return _columns.last();
}

QList<TableColumn*>::iterator Table::getFirstTableColumn() {
  return _columns.begin();
}

QList<TableColumn*>::iterator Table::getLastTableColumn() {
  return _columns.end();
}

PrimaryKey* Table::createPrimaryKey(const QString& n) {
  _primaryKey = new PrimaryKey(this, n);
  return _primaryKey;
}

UniqueConstraint* Table::createUniqueConstraint(const QString& n) {
  _uniqueConstraints.append(new UniqueConstraint(this, n));
  return _uniqueConstraints.last();
}

TextNotEmptyCheckConstraint* Table::createTextNotEmptyCheckConstraint(const QString& n) {
  _textNotEmptyCheckConstraints.append(new TextNotEmptyCheckConstraint(this, n));
  return _textNotEmptyCheckConstraints.last();
}

QString Table::getQualifiedName() {
   return QString("%1.%2").arg(getSchema()->getName()).arg(getName());
}

ForeignKey* Table::createForeignKey(const QString& name) {
  _foreignKeys.append(new ForeignKey(this, name));
  return _foreignKeys.last();
}

QList<ForeignKey*>::iterator Table::getFirstForeignKey() {
  return _foreignKeys.begin();
}

QList<ForeignKey*>::iterator Table::getLastForeignKey() {
  return _foreignKeys.end();
}

TableColumn* Table::getIdColumn() {
  if (!hasPrimaryKey()) {
    return 0;
  }

  return *(getPrimaryKey()->getFirstColumn());
}

TableColumn* Table::getTableColumn(const QString& name) {
  for (QList<TableColumn*>::iterator it = getFirstTableColumn(); it != getLastTableColumn(); it++) {
    TableColumn* c = *it;
    if (c->getName() == name) {
      return c;
    }
  }
  return 0;
}

