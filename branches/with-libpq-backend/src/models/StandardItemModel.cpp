/* 
 * File:   StandardItemModel.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:07
 */

#include "StandardItemModel.h"

#include <QApplication>

#include "ProfileLogger.h"
#include "Postgres.h"
#include "ProfileLoggerDatabase.h"

StandardItemModel::StandardItemModel(QObject* p)
  : QStandardItemModel(p),
    _dataManager(0),
    _postgres(0),
    _profileLoggerDatabase(0) {
  _postgres = (static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres();
  _profileLoggerDatabase = (static_cast<ProfileLogger*>(QApplication::instance()))->getProfileLoggerDatabase();
}

StandardItemModel::~StandardItemModel() {
}

void StandardItemModel::begin() {
  getPostgres()->begin();
}

void StandardItemModel::commit() {
  getPostgres()->commit();
}

void StandardItemModel::rollback() {
  getPostgres()->rollback();
}
QWidget* StandardItemModel::getDialogParent() {
  return QApplication::activeWindow();
}
