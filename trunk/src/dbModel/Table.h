#ifndef TABLE_H
#define TABLE_H

#include "DbInterfacePartInSchema.h"

#include "Database.h"

class Schema;
class TableColumn;
class PrimaryKey;
class UniqueConstraint;
class TextNotEmptyCheckConstraint;
class ForeignKey;

class Table: public DbInterfacePartInSchema {
  Q_OBJECT
    public:
  Table(Schema* s, const QString& name);
  virtual ~Table();

  TableColumn* createTableColumn(const QString& name, Database::DataTypes t);
  QList<TableColumn*>::iterator getFirstTableColumn();
  QList<TableColumn*>::iterator getLastTableColumn();

  ForeignKey* createForeignKey(const QString& name);
  QList<ForeignKey*>::iterator getFirstForeignKey();
  QList<ForeignKey*>::iterator getLastForeignKey();

  UniqueConstraint* createUniqueConstraint(const QString& name);
  QList<UniqueConstraint*>::iterator getFirstUniqueConstraint() {
    return _uniqueConstraints.begin();
  }

  QList<UniqueConstraint*>::iterator getLastUniqueConstraint() {
    return _uniqueConstraints.end();
  }

TextNotEmptyCheckConstraint* createTextNotEmptyCheckConstraint(const QString& name);
  QList<TextNotEmptyCheckConstraint*>::iterator getFirstTextNotEmptyCheckConstraint() {
    return _textNotEmptyCheckConstraints.begin();
  }

  QList<TextNotEmptyCheckConstraint*>::iterator getLastTextNotEmptyCheckConstraint() {
    return _textNotEmptyCheckConstraints.end();
  }

  PrimaryKey* createPrimaryKey(const QString& name);

  PrimaryKey* getPrimaryKey() {
    return _primaryKey;
  }

  bool hasPrimaryKey() const {
    return 0 != _primaryKey;
  }

  virtual QString getQualifiedName();

 private:
  QList<TableColumn*> _columns;
  QList<UniqueConstraint*> _uniqueConstraints;
  QList<TextNotEmptyCheckConstraint*> _textNotEmptyCheckConstraints;
  QList<ForeignKey*> _foreignKeys;

  PrimaryKey* _primaryKey;
};

#endif
