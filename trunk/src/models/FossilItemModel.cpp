/*
 * File:   FossilItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "FossilItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "FossilItem.h"
#include "Project.h"
#include "FossilEditorDialog.h"
#include "Fossil.h"

class Project;

FossilItemModel::FossilItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect(static_cast<ProfileLogger*> (QApplication::instance()),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

FossilItemModel::~FossilItemModel() {
}

void FossilItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void FossilItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Fossil");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }

    QList<Fossil*>::iterator it = _project->getFirstFossil();
    QList<Fossil*>::iterator last = _project->getLastFossil();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void FossilItemModel::createNew() {
    Fossil* p = _project->createFossil();
    FossilEditorDialog* dlg = new FossilEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

FossilItem* FossilItemModel::appendItem(Fossil* p) {
    FossilItem* i = new FossilItem(p);
    appendRow(i);
    return i;
}

void FossilItemModel::slotEditRequested(const QModelIndex& idx) {
    FossilItem* itm = (FossilItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    FossilEditorDialog* dlg = new FossilEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getFossil());
    dlg->exec();
    int id = dlg->getFossil()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForFossil(id)));
}

FossilItem* FossilItemModel::findItemForFossil(int id) {
    for (int r = 0; r < rowCount(); r++) {
        FossilItem* ret = (FossilItem*) item(r);
        if (ret->getFossil()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void FossilItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        FossilItem* itm = (FossilItem*) itemFromIndex(*it);
        _project->deleteFossil(itm->getFossil());
    }
    reload();
}

QModelIndex FossilItemModel::findIndexForFossil(Fossil* q) {
    if (!q) {
        return QModelIndex();
    }

    FossilItem* itm = findItemForFossil(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
