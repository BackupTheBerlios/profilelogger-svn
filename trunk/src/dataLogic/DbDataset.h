#ifndef DBDATASET_H
#define DBDATASET_H

#include <QCoreApplication>

#include <QString>

#include "ProfileLogger.h"

class ProfileLoggerDatabase;
class DatabaseConnection;
class Sequence;
class Table;

class DbDataset {
  Q_DECLARE_TR_FUNCTIONS(DbDataset);

 public:
  DbDataset(const int id = 0);
  virtual ~DbDataset() {}

  const bool hasId() {
    return _id > 0;
  }

  void setId(const int id) {
    _isDirty = true;
    _id = id;
  }

  int getId() const {
    return _id;
  }

  bool getIsDirty() const {
    return _isDirty;
  }

  void setIsDirty(bool dirty) {
    _isDirty = dirty;
  }

  virtual QString toString() const;

  virtual void save();
  virtual void refresh() = 0;
  virtual void remove() = 0;

 protected:
  virtual void insert() = 0;
  virtual void update() = 0;
  virtual void getAndSetIdFromDb();

  void setSequence(Sequence* s) {
    _seq = s;
  }

  Sequence* getSequence() const {
    return _seq;
  }

  void setTable(Table* t) {
    _table = t;
  }
  
  Table* getTable() const {
    return _table;
  }

  ProfileLogger* getApp() const;
  ProfileLoggerDatabase* getDb() const;
  DatabaseConnection* getDbConn() const;

 private:
  int _id;
  bool _isDirty;
  Sequence* _seq;
  Table* _table;
};

#endif
