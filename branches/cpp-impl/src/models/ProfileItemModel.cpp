/* 
 * File:   ProfileItemModel.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:12
 */

#include "ProfileItemModel.h"

#include <QApplication>
#include <QItemSelectionModel>
#include <QMainWindow>
#include <QMessageBox>

#include "WorkWidget.h"
#include "Profile.h"
#include "ProfileItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "ProfileEditorDialog.h"
#include "XMLInterface.h"
#include "CsvInterface.h"

ProfileItemModel::ProfileItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    reload();

    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

ProfileItemModel::~ProfileItemModel() {
}

void ProfileItemModel::reload() {
    clear();
    if (!_project) {
        return;
    }

    if (!_project) {
        return;
    }

    QStringList hh;
    hh << tr("Profile");
    setHorizontalHeaderLabels(hh);

    QList<Profile*>::iterator it = _project->getFirstProfile();
    QList<Profile*>::iterator last = _project->getLastProfile();
    
    while(it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void ProfileItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void ProfileItemModel::createNew() {
    Profile* p = _project->createProfile();
    ProfileEditorDialog* dlg = new ProfileEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

ProfileItem* ProfileItemModel::appendItem(Profile* p) {
    ProfileItem* i = new ProfileItem(p);
    appendRow(i);
    return i;
}

void ProfileItemModel::slotEditRequested(const QModelIndex& idx) {
    ProfileItem* itm = (ProfileItem*)itemFromIndex(idx);

    if (!itm) {
        return;
    }

    ProfileEditorDialog* dlg = new ProfileEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getProfile());
    dlg->exec();
    int id = dlg->getProfile()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForProfile(id)));
}

ProfileItem* ProfileItemModel::findItemForProfile(int id) {
    for (int r = 0; r < rowCount(); r++) {
        ProfileItem* ret = (ProfileItem*)item(r);
        if (ret->getProfile()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void ProfileItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        ProfileItem* itm = (ProfileItem*)itemFromIndex(*it);
        _project->deleteProfile(itm->getProfile());
    }
    reload();
}

void ProfileItemModel::slotDuplicateRequested(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    ProfileItem* itm = (ProfileItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    _project->duplicateProfile(itm->getProfile());
    reload();
}

void ProfileItemModel::slotImportFromCsvFileRequested(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    ProfileItem* itm = (ProfileItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    itm->getProfile()->importBedsFromCsvFile();
    reload();
}

QModelIndex ProfileItemModel::findIndexForProfile(Profile* q) {
    if (!q) {
        return QModelIndex();
    }

    ProfileItem* itm = findItemForProfile(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
