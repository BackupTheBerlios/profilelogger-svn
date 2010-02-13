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

class Project;

LithologyItemModel::LithologyItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect(static_cast<ProfileLogger*> (QApplication::instance()),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

LithologyItemModel::~LithologyItemModel() {
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

    QList<Lithology*>::iterator it = _project->getFirstLithology();
    QList<Lithology*>::iterator last = _project->getLastLithology();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void LithologyItemModel::createNew() {
    Lithology* p = _project->createLithology();
    LithologyEditorDialog* dlg = new LithologyEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
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

    LithologyEditorDialog* dlg = new LithologyEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getLithology());
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
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        LithologyItem* itm = (LithologyItem*) itemFromIndex(*it);
        _project->deleteLithology(itm->getLithology());
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
