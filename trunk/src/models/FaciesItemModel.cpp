/*
 * File:   FaciesItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "FaciesItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "FaciesItem.h"
#include "Project.h"
#include "FaciesEditorDialog.h"
#include "Facies.h"

class Project;

FaciesItemModel::FaciesItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

FaciesItemModel::~FaciesItemModel() {
}

void FaciesItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void FaciesItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Facies");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }

    QList<Facies*>::iterator it = _project->getFirstFacies();
    QList<Facies*>::iterator last = _project->getLastFacies();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void FaciesItemModel::createNew() {
    Facies* p = _project->createFacies();
    FaciesEditorDialog* dlg = new FaciesEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

FaciesItem* FaciesItemModel::appendItem(Facies* p) {
    FaciesItem* i = new FaciesItem(p);
    appendRow(i);
    return i;
}

void FaciesItemModel::slotEditRequested(const QModelIndex& idx) {
    FaciesItem* itm = (FaciesItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    FaciesEditorDialog* dlg = new FaciesEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getFacies());
    dlg->exec();
    int id = dlg->getFacies()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForFacies(id)));
}

FaciesItem* FaciesItemModel::findItemForFacies(int id) {
    for (int r = 0; r < rowCount(); r++) {
        FaciesItem* ret = (FaciesItem*) item(r);
        if (ret->getFacies()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void FaciesItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        FaciesItem* itm = (FaciesItem*) itemFromIndex(*it);
        _project->deleteFacies(itm->getFacies());
    }
    reload();
}

QModelIndex FaciesItemModel::findIndexForFacies(Facies* q) {
    if (!q) {
        return QModelIndex();
    }

    FaciesItem* itm = findItemForFacies(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
