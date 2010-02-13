/*
 * File:   BoundaryTypeItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "BoundaryTypeItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "BoundaryTypeItem.h"
#include "Project.h"
#include "BoundaryTypeEditorDialog.h"
#include "BoundaryType.h"

class Project;

BoundaryTypeItemModel::BoundaryTypeItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

BoundaryTypeItemModel::~BoundaryTypeItemModel() {
}

void BoundaryTypeItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void BoundaryTypeItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Boundary Type");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }

    QList<BoundaryType*>::iterator it = _project->getFirstBoundaryType();
    QList<BoundaryType*>::iterator last = _project->getLastBoundaryType();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void BoundaryTypeItemModel::createNew() {
    BoundaryType* p = _project->createBoundaryType();
    BoundaryTypeEditorDialog* dlg = new BoundaryTypeEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

BoundaryTypeItem* BoundaryTypeItemModel::appendItem(BoundaryType* p) {
    BoundaryTypeItem* i = new BoundaryTypeItem(p);
    appendRow(i);
    return i;
}

void BoundaryTypeItemModel::slotEditRequested(const QModelIndex& idx) {
    BoundaryTypeItem* itm = (BoundaryTypeItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    BoundaryTypeEditorDialog* dlg = new BoundaryTypeEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getBoundaryType());
    dlg->exec();
    int id = dlg->getBoundaryType()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForBoundaryType(id)));
}

BoundaryTypeItem* BoundaryTypeItemModel::findItemForBoundaryType(int id) {
    for (int r = 0; r < rowCount(); r++) {
        BoundaryTypeItem* ret = (BoundaryTypeItem*) item(r);
        if (ret->getBoundaryType()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void BoundaryTypeItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        BoundaryTypeItem* itm = (BoundaryTypeItem*) itemFromIndex(*it);
        _project->deleteBoundaryType(itm->getBoundaryType());
    }
    reload();
}

QModelIndex BoundaryTypeItemModel::findIndexForBoundaryType(BoundaryType* q) {
    if (!q) {
        return QModelIndex();
    }

    BoundaryTypeItem* itm = findItemForBoundaryType(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
