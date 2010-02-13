/*
 * File:   ClasticGrainSizeItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "ClasticGrainSizeItemModel.h"

#include <QApplication>

#include "ProfileLogger.h"
#include "ClasticGrainSizeItem.h"
#include "Project.h"
#include "ClasticGrainSize.h"

class Project;

ClasticGrainSizeItemModel::ClasticGrainSizeItemModel(QObject* p)
: GrainSizeItemModel(p),
_project(0) {
    connect(static_cast<ProfileLogger*> (QApplication::instance()),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

ClasticGrainSizeItemModel::~ClasticGrainSizeItemModel() {
}

void ClasticGrainSizeItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void ClasticGrainSizeItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Clastic Grain Size");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }
    
    QList<ClasticGrainSize*>::iterator it = _project->getFirstClasticGrainSize();
    QList<ClasticGrainSize*>::iterator last = _project->getLastClasticGrainSize();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

ClasticGrainSizeItem* ClasticGrainSizeItemModel::appendItem(ClasticGrainSize* p) {
    ClasticGrainSizeItem* i = new ClasticGrainSizeItem(p);
    appendRow(i);
    return i;
}

ClasticGrainSizeItem* ClasticGrainSizeItemModel::findItemForClasticGrainSize(int id) {
    for (int r = 0; r < rowCount(); r++) {
        ClasticGrainSizeItem* ret = (ClasticGrainSizeItem*) item(r);
        if (ret->getClasticGrainSize()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

QModelIndex ClasticGrainSizeItemModel::findIndexForClasticGrainSize(ClasticGrainSize* q) {
    if (!q) {
        return QModelIndex();
    }

    ClasticGrainSizeItem* itm = findItemForClasticGrainSize(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
