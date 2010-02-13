/* 
 * File:   ProfileCorrelationItemModel.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:12
 */

#include "ProfileCorrelationItemModel.h"

#include <QApplication>
#include <QItemSelectionModel>
#include <QMessageBox>

#include "MainWindow.h"
#include "WorkWidget.h"
#include "ProfileCorrelation.h"
#include "ProfileCorrelationItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "ProfileCorrelationEditorDialog.h"
#include "XMLInterface.h"

ProfileCorrelationItemModel::ProfileCorrelationItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    reload();

    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

ProfileCorrelationItemModel::~ProfileCorrelationItemModel() {
}

void ProfileCorrelationItemModel::reload() {
    clear();
    if (!_project) {
        return;
    }

    if (!_project) {
        return;
    }

    QStringList hh;
    hh << tr("ProfileCorrelation");
    setHorizontalHeaderLabels(hh);

    QList<ProfileCorrelation*>::iterator it = _project->getFirstProfileCorrelation();
    QList<ProfileCorrelation*>::iterator last = _project->getLastProfileCorrelation();
    
    while(it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void ProfileCorrelationItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void ProfileCorrelationItemModel::createNew() {
    ProfileCorrelation* p = _project->createProfileCorrelation();
    ProfileCorrelationEditorDialog* dlg = new ProfileCorrelationEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

ProfileCorrelationItem* ProfileCorrelationItemModel::appendItem(ProfileCorrelation* p) {
    ProfileCorrelationItem* i = new ProfileCorrelationItem(p);
    appendRow(i);
    return i;
}

void ProfileCorrelationItemModel::slotEditRequested(const QModelIndex& idx) {
    ProfileCorrelationItem* itm = (ProfileCorrelationItem*)itemFromIndex(idx);

    if (!itm) {
        return;
    }

    ProfileCorrelationEditorDialog* dlg = new ProfileCorrelationEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getProfileCorrelation());
    dlg->exec();
    int id = dlg->getProfileCorrelation()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForProfileCorrelation(id)));
}

ProfileCorrelationItem* ProfileCorrelationItemModel::findItemForProfileCorrelation(int id) {
    for (int r = 0; r < rowCount(); r++) {
        ProfileCorrelationItem* ret = (ProfileCorrelationItem*)item(r);
        if (ret->getProfileCorrelation()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void ProfileCorrelationItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        ProfileCorrelationItem* itm = (ProfileCorrelationItem*)itemFromIndex(*it);
        _project->deleteProfileCorrelation(itm->getProfileCorrelation());
    }
    reload();
}

void ProfileCorrelationItemModel::slotDuplicateRequested(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    ProfileCorrelationItem* itm = (ProfileCorrelationItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    _project->duplicateProfileCorrelation(itm->getProfileCorrelation());
    reload();
}
