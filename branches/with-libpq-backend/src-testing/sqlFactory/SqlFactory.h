#ifndef SQL_FACTORY_H
#define SQL_FACTORY_H

#include <QObject>

#include <QStringList>

#include "TableColumn.h"

#include "Database.h"

class Schema;
class Sequence;
class Table;
class UniqueConstraint;
class TextNotEmptyCheckConstraint;
class PrimaryKey;
class ForeignKey;

class SqlFactory: public QObject
{
  Q_OBJECT
    public:
  SqlFactory(QObject* p);
  virtual ~SqlFactory();

  void setDatabase(Database* d) {
    _database = d;
  }

  Database* getDatabase() {
    return _database;
  }

  const bool hasDatabase() {
    return 0 != _database;
  }

  QString typeToString(Database::DataTypes t);

  QStringList make(Database* db);
  QStringList drop(Schema* s);
  QStringList make(Schema* s);
  QStringList make(Sequence* s);
  QStringList make(Table* t);
  QStringList make(UniqueConstraint* u);
  QStringList make(TextNotEmptyCheckConstraint* c);
  QStringList make(PrimaryKey* p);
  QStringList make(ForeignKey* f);
  QString makeDefaultFromSequence(TableColumn* c);
  QString makeDefaultText(TableColumn* c);
  QString makeDefaultInt(TableColumn* c);
  QString makeDefaultDouble(TableColumn* c);
  QString makeDefaultFromConstant(TableColumn* c);

  QString makeNextval(Sequence* s, const QString& as);

  QString makeSelectAll(Table* t,
			QList<TableColumn*> order = QList<TableColumn>());

  QString makeSelectById(Table* t,
			 QList<TableColumn*> colsToSelect,
			 QStringList selectColsAs,
			 TableColumn* idCol,
			 const int id);

  QString makeDelete(Table* t, 
		     const QString& idPlaceholder = "id");

  QString makeInsert(Table* t, 
		     QList<TableColumn*> cols, 
		     QStringList placeholders);

  QString makeUpdate(Table* t, 
		     QList<TableColumn*> valueCols, 
		     QStringList placeholders,
		     const QString& idPlaceholder = ":id");
  
 protected:
  QString quoteIdentifier(const QString& s);

 private:
  Database* _database;
};

#endif
