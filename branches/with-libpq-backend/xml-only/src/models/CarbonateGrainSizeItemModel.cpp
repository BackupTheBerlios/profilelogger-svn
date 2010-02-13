/*
 * File:   CarbonateGrainSizeItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "CarbonateGrainSizeItemModel.h"

#include <QApplication>

#include "ProfileLogger.h"
#include "CarbonateGrainSizeItem.h"
#include "Project.h"
#include "CarbonateGrainSize.h"

class Project;

CarbonateGrainSizeItemModel::CarbonateGrainSizeItemModel(QObject* p)
: GrainSizeItemModel(p),
_project(0) {
    connect(static_cast<ProfileLogger*> (QApplication::instance()),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

CarbonateGrainSizeItemModel::~CarbonateGrainSizeItemModel() {
}

void CarbonateGrainSizeItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void CarbonateGrainSizeItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Carbonate Grain Size");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }

    QList<CarbonateGrainSize*>::iterator it = _project->getFirstCarbonateGrainSize();
    QList<CarbonateGrainSize*>::iterator last = _project->getLastCarbonateGrainSize();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

CarbonateGrainSizeItem* CarbonateGrainSizeItemModel::appendItem(CarbonateGrainSize* p) {
    CarbonateGrainSizeItem* i = new CarbonateGrainSizeItem(p);
    appendRow(i);
    return i;
}

CarbonateGrainSizeItem* CarbonateGrainSizeItemModel::findItemForCarbonateGrainSize(int id) {
    for (int r = 0; r < rowCount(); r++) {
        CarbonateGrainSizeItem* ret = (CarbonateGrainSizeItem*) item(r);
        if (ret->getCarbonateGrainSize()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

QModelIndex CarbonateGrainSizeItemModel::findIndexForCarbonateGrainSize(CarbonateGrainSize* q) {
    if (!q) {
        return QModelIndex();
    }

    CarbonateGrainSizeItem* itm = findItemForCarbonateGrainSize(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
