/*
 * File:   LithologicalUnitItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "LithologicalUnitItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "LithologicalUnitItem.h"
#include "Project.h"
#include "LithologicalUnitEditorDialog.h"
#include "LithologicalUnit.h"

class Project;

LithologicalUnitItemModel::LithologicalUnitItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

LithologicalUnitItemModel::~LithologicalUnitItemModel() {
}

void LithologicalUnitItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void LithologicalUnitItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Lithological Unit");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }

    QList<LithologicalUnit*>::iterator it = _project->getFirstLithologicalUnit();
    QList<LithologicalUnit*>::iterator last = _project->getLastLithologicalUnit();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void LithologicalUnitItemModel::createNew() {
    LithologicalUnit* p = _project->createLithologicalUnit();
    LithologicalUnitEditorDialog* dlg = new LithologicalUnitEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

LithologicalUnitItem* LithologicalUnitItemModel::appendItem(LithologicalUnit* p) {
    LithologicalUnitItem* i = new LithologicalUnitItem(p);
    appendRow(i);
    return i;
}

void LithologicalUnitItemModel::slotEditRequested(const QModelIndex& idx) {
    LithologicalUnitItem* itm = (LithologicalUnitItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    LithologicalUnitEditorDialog* dlg = new LithologicalUnitEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getLithologicalUnit());
    dlg->exec();
    int id = dlg->getLithologicalUnit()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForLithologicalUnit(id)));
}

LithologicalUnitItem* LithologicalUnitItemModel::findItemForLithologicalUnit(int id) {
    for (int r = 0; r < rowCount(); r++) {
        LithologicalUnitItem* ret = (LithologicalUnitItem*) item(r);
        if (ret->getLithologicalUnit()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void LithologicalUnitItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        LithologicalUnitItem* itm = (LithologicalUnitItem*) itemFromIndex(*it);
        _project->deleteLithologicalUnit(itm->getLithologicalUnit());
    }
    reload();
}

QModelIndex LithologicalUnitItemModel::findIndexForLithologicalUnit(LithologicalUnit* q) {
    if (!q) {
        return QModelIndex();
    }

    LithologicalUnitItem* itm = findItemForLithologicalUnit(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
