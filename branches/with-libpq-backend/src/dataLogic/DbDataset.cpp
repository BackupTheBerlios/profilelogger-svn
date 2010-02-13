#include "DbDataset.h"

#include <QSqlQuery>
#include <QSqlRecord>

#include "ProfileLogger.h"
#include "ProfileLoggerDatabase.h"
#include "DatabaseConnection.h"

#include "DatabaseConnection.h"
#include "SqlFactory.h"

DbDataset::DbDataset(const int id)
  : _id(id),
    _isDirty(false),
    _seq(0),
    _table(0)
{}

QString DbDataset::toString() const {
  return tr("ID: %1").arg(_id);
}

ProfileLogger* DbDataset::getApp() const {
  return static_cast<ProfileLogger*>(QApplication::instance());
}

ProfileLoggerDatabase* DbDataset::getDb() const {
  return getApp()->getProfileLoggerDatabase();
}

DatabaseConnection* DbDataset::getDbConn() const {
  return getApp()->getDatabaseConnection();
}


void DbDataset::save() {
  if (!getIsDirty()) {
    return;
  }

  if (!hasId()) {
    getAndSetIdFromDb();
    insert();
  } else {
    update();
  }

  refresh();
}

void DbDataset::getAndSetIdFromDb() {
  SqlFactory f(getApp());

  QSqlQuery q = getDbConn()->createQuery(f.makeNextval(getSequence(), "id"));
  getDbConn()->execSelect(&q, 1);
  q.first();

  QSqlRecord r = q.record();
  int i = r.indexOf("id");
  setId(r.value(i).toInt());
}
