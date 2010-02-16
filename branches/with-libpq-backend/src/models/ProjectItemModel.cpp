/* 
 * File:   ProjectItemModel.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:12
 */

#include "ProjectItemModel.h"

#include <QApplication>
#include <QItemSelectionModel>
#include <QMainWindow>
#include <QMessageBox>
#include <QApplication>
#include <QDebug>

#include "WorkWidget.h"
#include "Project.h"
#include "ProjectItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "ProjectEditorDialog.h"
#include "MainWindow.h"
#include "ProjectManager.h"
#include "Postgres.h"
#include "DatabaseErrorDialog.h"
#include "DatabaseError.h"
#include "ProjectManager.h"

ProjectItemModel::ProjectItemModel(QObject* p)
  : StandardItemModel(p) {
  setDataManager(new ProjectManager(this,
				    getPostgres(),
				    getProfileLoggerDatabase()));
}

ProjectManager* ProjectItemModel::getProjectManager() {
  return (ProjectManager*)getDataManager();
}

ProjectItemModel::~ProjectItemModel() {
}

void ProjectItemModel::reload() {
  clear();
  _projects.clear();

  QStringList hh;
  hh << tr("Project");
  setHorizontalHeaderLabels(hh);
    
  try {
    begin();
    _projects = getProjectManager()->loadProjects();
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

  QList<Project*>::iterator it = getFirstProject();
  QList<Project*>::iterator last = getLastProject();
    
  while(it != last) {
    appendItem(*it);
    it++;
  }

  emit reloaded();
}

void ProjectItemModel::createNew() {
  Project* p = new Project();

  ProjectEditorDialog* dlg = new ProjectEditorDialog(getDialogParent(), p);
  if (QDialog::Accepted != dlg->exec()) {
    _projects.removeLast();
    return;
  }

  int id = p->getId();

  delete p;

  reload();

  emit selectItemRequest(indexFromItem(findItemForProject(id)));
}

ProjectItem* ProjectItemModel::appendItem(Project* p) {
  ProjectItem* i = new ProjectItem(p);
  appendRow(i);
  return i;
}

void ProjectItemModel::slotEditRequested(const QModelIndex& idx) {
  ProjectItem* itm = (ProjectItem*)itemFromIndex(idx);

  if (!itm) {
    return;
  }

  ProjectEditorDialog* dlg = new ProjectEditorDialog(getDialogParent(), 
						     itm->getProject());
  dlg->exec();

  int id = dlg->getProject()->getId();

  reload();

  emit selectItemRequest(indexFromItem(findItemForProject(id)));
}

ProjectItem* ProjectItemModel::findItemForProject(int id) {
  for (int r = 0; r < rowCount(); r++) {
    ProjectItem* ret = (ProjectItem*)item(r);
    if (ret->getProject()->getId() == id) {
      return ret;
    }
  }
  return 0;
}

void ProjectItemModel::slotDeleteRequested(QModelIndexList list) {
  try {
    for (QModelIndexList::iterator it = list.begin();
	 it != list.end();
	 it++) {
      begin();      
      ProjectItem* itm = (ProjectItem*)itemFromIndex(*it);
      Project* p = itm->getProject();
      getProjectManager()->remove(p);
  
      int idx = _projects.indexOf(p);

      if (idx != -1) {
	_projects.removeAt(idx);

	if (p) {
	  delete p;
	}
      }

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
  void ProjectItemModel::slotDuplicateRequested(const QModelIndex& idx) {
    if (!idx.isValid()) {
      return;
    }

    ProjectItem* itm = (ProjectItem*) itemFromIndex(idx);

    if (!itm) {
      return;
    }

    //_project->duplicateProject(itm->getProject());
    reload();
  }

  QModelIndex ProjectItemModel::findIndexForProject(Project* q) {
    if (!q) {
      return QModelIndex();
    }

    ProjectItem* itm = findItemForProject(q->getId());
    if (!itm) {
      return QModelIndex();
    }
    return indexFromItem(itm);
  }

  QList<Project*>::iterator ProjectItemModel::getFirstProject() {
    return _projects.begin();
  }

  QList<Project*>::iterator ProjectItemModel::getLastProject() {
    return _projects.end();
  }
