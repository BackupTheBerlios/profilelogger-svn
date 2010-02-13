#ifndef DATAMANAGER_H
#define DATAMANAGER_H

#include <QObject>

#include <QStringList>
#include <QVariant>

class Postgres;
class AppDatabase;
class SqlFactory;

class Dataset;
class Table;
class TableColumn;

class DataManager: public QObject
{
  Q_OBJECT
    public:
  DataManager(QObject* p, Postgres* pg, AppDatabase* dm);
  virtual ~DataManager() {}

  Postgres* getPostgres() const {
    return _pg;
  }

  virtual QStringList getInsertPlaceholders() const {
    return QStringList();
  }

  virtual QList<TableColumn*> getInsertColumns() const {
    return QList<TableColumn*>();
  }

  virtual QList<TableColumn*> getUpdateColumns() const {
    return QList<TableColumn*>();
  }

  virtual QList<TableColumn*> getSelectColumns() const {
    return QList<TableColumn*>();
  }

  virtual QList<TableColumn*> getGroupByColumns() const {
    return QList<TableColumn*>();
  }

  virtual QList<TableColumn*> getOrderByColumns() const {
    return QList<TableColumn*>();
  }

  AppDatabase* getDbModel() const {
    return _dm;
  }

  void setTable(Table* t) {
    _table = t;
  }

  Table* getTable() const {
    return _table;
  }

  virtual void remove(Dataset* d);

  SqlFactory* getSqlFactory() const {
    return _sqlF;
  }

 protected:
  QString makePlaceholder(const int placeholderNumber, TableColumn* col) const;
  void performInsert(Table* t,
		     QList<TableColumn*> cols,
		     const QStringList& placeholders,
		     const QVariantList& values);
  void performUpdate(Table* t,
		     QList<TableColumn*> updateCols,
		     const QStringList& updatePlaceholders,
		     const QVariantList& updateValues,
		     TableColumn* idCol,
		     const QString& idPlaceholder,
		     const int id);
    private:
  Postgres* _pg;
  AppDatabase* _dm;
  Table* _table;
  SqlFactory* _sqlF;
};

#endif
