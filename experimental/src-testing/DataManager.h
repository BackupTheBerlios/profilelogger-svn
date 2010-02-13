#ifndef DATAMANAGER_H
#define DATAMANAGER_H

#include <QObject>

#include <QStringList>

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

  virtual QStringList getInsertColumns() const {
    return QStringList();
  }

  virtual QStringList getUpdateColumns() const {
    return QStringList();
  }

  virtual QStringList getSelectColumns() const {
    return QStringList();
  }

  virtual QStringList getGroupByColumns() const {
    return QStringList();
  }

  virtual QStringList getOrderByColumns() const {
    return QStringList();
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

  QString makePlaceholder(const int placeholderNumber, TableColumn* col) const;

 private:
  Postgres* _pg;
  AppDatabase* _dm;
  Table* _table;
  SqlFactory* _sqlF;
};

#endif
