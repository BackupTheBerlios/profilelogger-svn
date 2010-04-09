/*
 * File:   SedimentStructureItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "SedimentStructureItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "SedimentStructureItem.h"
#include "Project.h"
#include "SedimentStructureEditorDialog.h"
#include "SedimentStructure.h"

class Project;

SedimentStructureItemModel::SedimentStructureItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect(static_cast<ProfileLogger*> (QApplication::instance()),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

SedimentStructureItemModel::~SedimentStructureItemModel() {
}

void SedimentStructureItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void SedimentStructureItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Sediment Structure");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }
    
    QList<SedimentStructure*>::iterator it = _project->getFirstSedimentStructure();
    QList<SedimentStructure*>::iterator last = _project->getLastSedimentStructure();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void SedimentStructureItemModel::createNew() {
    SedimentStructure* p = _project->createSedimentStructure();
    SedimentStructureEditorDialog* dlg = new SedimentStructureEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

SedimentStructureItem* SedimentStructureItemModel::appendItem(SedimentStructure* p) {
    SedimentStructureItem* i = new SedimentStructureItem(p);
    appendRow(i);
    return i;
}

void SedimentStructureItemModel::slotEditRequested(const QModelIndex& idx) {
    SedimentStructureItem* itm = (SedimentStructureItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    SedimentStructureEditorDialog* dlg = new SedimentStructureEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getSedimentStructure());
    dlg->exec();
    int id = dlg->getSedimentStructure()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForSedimentStructure(id)));
}

SedimentStructureItem* SedimentStructureItemModel::findItemForSedimentStructure(int id) {
    for (int r = 0; r < rowCount(); r++) {
        SedimentStructureItem* ret = (SedimentStructureItem*) item(r);
        if (ret->getSedimentStructure()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void SedimentStructureItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        SedimentStructureItem* itm = (SedimentStructureItem*) itemFromIndex(*it);
        _project->deleteSedimentStructure(itm->getSedimentStructure());
    }
    reload();
}

QModelIndex SedimentStructureItemModel::findIndexForSedimentStructure(SedimentStructure* q) {
    if (!q) {
        return QModelIndex();
    }

    SedimentStructureItem* itm = findItemForSedimentStructure(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
