/*
 * File:   LithologicalUnitTypeItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "LithologicalUnitTypeItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "LithologicalUnitTypeItem.h"
#include "Project.h"
#include "LithologicalUnitTypeEditorDialog.h"
#include "LithologicalUnitType.h"

class Project;

LithologicalUnitTypeItemModel::LithologicalUnitTypeItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

LithologicalUnitTypeItemModel::~LithologicalUnitTypeItemModel() {
}

void LithologicalUnitTypeItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void LithologicalUnitTypeItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Lithological Unit Type");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }
    
    QList<LithologicalUnitType*>::iterator it = _project->getFirstLithologicalUnitType();
    QList<LithologicalUnitType*>::iterator last = _project->getLastLithologicalUnitType();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void LithologicalUnitTypeItemModel::createNew() {
    LithologicalUnitType* p = _project->createLithologicalUnitType();
    LithologicalUnitTypeEditorDialog* dlg = new LithologicalUnitTypeEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

LithologicalUnitTypeItem* LithologicalUnitTypeItemModel::appendItem(LithologicalUnitType* p) {
    LithologicalUnitTypeItem* i = new LithologicalUnitTypeItem(p);
    appendRow(i);
    return i;
}

void LithologicalUnitTypeItemModel::slotEditRequested(const QModelIndex& idx) {
    LithologicalUnitTypeItem* itm = (LithologicalUnitTypeItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    LithologicalUnitTypeEditorDialog* dlg = new LithologicalUnitTypeEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getLithologicalUnitType());
    dlg->exec();
    int id = dlg->getLithologicalUnitType()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForLithologicalUnitType(id)));
}

LithologicalUnitTypeItem* LithologicalUnitTypeItemModel::findItemForLithologicalUnitType(int id) {
    for (int r = 0; r < rowCount(); r++) {
        LithologicalUnitTypeItem* ret = (LithologicalUnitTypeItem*) item(r);
        if (ret->getLithologicalUnitType()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void LithologicalUnitTypeItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        LithologicalUnitTypeItem* itm = (LithologicalUnitTypeItem*) itemFromIndex(*it);
        _project->deleteLithologicalUnitType(itm->getLithologicalUnitType());
    }
    reload();
}

QModelIndex LithologicalUnitTypeItemModel::findIndexForLithologicalUnitType(LithologicalUnitType* q) {
    if (!q) {
        return QModelIndex();
    }

    LithologicalUnitTypeItem* itm = findItemForLithologicalUnitType(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
