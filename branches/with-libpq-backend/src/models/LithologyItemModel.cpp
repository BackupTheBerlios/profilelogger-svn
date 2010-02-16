/*
 * File:   LithologyItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "LithologyItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "LithologyItem.h"
#include "Project.h"
#include "LithologyEditorDialog.h"
#include "Lithology.h"
#include "LithologyManager.h"
#include "DatabaseError.h"
#include "DatabaseErrorDialog.h"

class Project;

LithologyItemModel::LithologyItemModel(QObject* p)
  : StandardItemModel(p),
    _project(0) {
  setDataManager(new LithologyManager(this,
				      getPostgres(),
				      getProfileLoggerDatabase()));
}

LithologyItemModel::~LithologyItemModel() {
}

LithologyManager* LithologyItemModel::getLithologyManager() {
  return (LithologyManager*)getDataManager();
}

void LithologyItemModel::slotCurrentProjectChanged(Project* p) {
  _project = p;
  reload();
}

void LithologyItemModel::reload() {
  clear();

  QStringList hh;
  hh << tr("Lithology");
  setHorizontalHeaderLabels(hh);

  if (!_project) {
    return;
  }

  try {
    begin();
    _project->setLithologies(getLithologyManager()->loadLithologies(_project));
    commit();
  }
  catch(DatabaseError e) {
    DatabaseErrorDialog dlg(getDialogParent(), e);
    dlg.exec();
    try {
      rollback();
    }
    catch(DatabaseError e) {
      DatabaseErrorDialog dlg(getDialogParent(), e);
      dlg.exec();
    }
  }
  QList<Lithology*>::iterator it = _project->getFirstLithology();
  QList<Lithology*>::iterator last = _project->getLastLithology();

  while (it != last) {
    appendItem(*it);
    it++;
  }

  emit reloaded();
}

void LithologyItemModel::createNew() {
  Q_ASSERT(_project);
  Lithology* p = new Lithology(_project);
  
  LithologyEditorDialog* dlg = new LithologyEditorDialog(getDialogParent(), p);
  
  if (QDialog::Accepted != dlg->exec()) {
    delete p;
    return;
  }

  int id = p->getId();
    
  if (p) {
    delete p;
  }

  reload();

  emit selectItemRequest(indexFromItem(findItemForLithology(id)));
}

LithologyItem* LithologyItemModel::appendItem(Lithology* p) {
  LithologyItem* i = new LithologyItem(p);
  appendRow(i);
  return i;
}

void LithologyItemModel::slotEditRequested(const QModelIndex& idx) {
  LithologyItem* itm = (LithologyItem*) itemFromIndex(idx);

  if (!itm) {
    return;
  }

  LithologyEditorDialog* dlg = new LithologyEditorDialog(getDialogParent(), 
							 itm->getLithology());
  dlg->exec();

  int id = dlg->getLithology()->getId();

  reload();

  emit selectItemRequest(indexFromItem(findItemForLithology(id)));
}

LithologyItem* LithologyItemModel::findItemForLithology(int id) {
  for (int r = 0; r < rowCount(); r++) {
    LithologyItem* ret = (LithologyItem*) item(r);
    if (ret->getLithology()->getId() == id) {
      return ret;
    }
  }
  return 0;
}

void LithologyItemModel::slotDeleteRequested(QModelIndexList list) {
  try {
    for (QModelIndexList::iterator it = list.begin(); it != list.end(); it++) {
      begin();
      LithologyItem* itm = (LithologyItem*) itemFromIndex(*it);
      Lithology* l = itm->getLithology();
      getLithologyManager()->remove(l);
      _project->deleteLithology(l);
      commit();
    }
  }
  catch(DatabaseError e) {
    DatabaseErrorDialog dlg(QApplication::activeWindow(), e);
    dlg.exec();
    
    try {
      rollback();
    }
    catch(DatabaseError e) {
      DatabaseErrorDialog dlg(getDialogParent(), e);
      dlg.exec();
    }
  }

  reload();
}

QModelIndex LithologyItemModel::findIndexForLithology(Lithology* q) {
  if (!q) {
    return QModelIndex();
  }

  LithologyItem* itm = findItemForLithology(q->getId());
  if (!itm) {
    return QModelIndex();
  }
  return indexFromItem(itm);
}
