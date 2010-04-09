/*
 * File:   SedimentStructureInBedItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "SedimentStructureInBedItemModel.h"

#include <QApplication>
#include <QMimeData>

#include "ProfileLogger.h"
#include "SedimentStructureItem.h"
#include "Project.h"
#include "Bed.h"
#include "SedimentStructureEditorDialog.h"
#include "SedimentStructure.h"

class Project;

SedimentStructureInBedItemModel::SedimentStructureInBedItemModel(QObject* p)
: StandardItemModel(p),
_bed(0) {
}

SedimentStructureInBedItemModel::~SedimentStructureInBedItemModel() {
}

void SedimentStructureInBedItemModel::slotCurrentBedChanged(Bed* b) {
    _bed = b;
    reload();
}

void SedimentStructureInBedItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Sediment Structure");
    setHorizontalHeaderLabels(hh);

    if (!_bed) {
        return;
    }

    QList<SedimentStructure*>::iterator it = _bed->getFirstSedimentStructure();
    QList<SedimentStructure*>::iterator last = _bed->getLastSedimentStructure();

    while (it != last) {
        SedimentStructure* f = *it;
        if (f) {
            appendItem(*it);
        }
        it++;
    }

    emit reloaded();
}

SedimentStructureItem* SedimentStructureInBedItemModel::appendItem(SedimentStructure* p) {
    SedimentStructureItem* i = new SedimentStructureItem(p);
    appendRow(i);
    return i;
}

SedimentStructureItem* SedimentStructureInBedItemModel::findItemForSedimentStructure(int id) {
    for (int r = 0; r < rowCount(); r++) {
        SedimentStructureItem* ret = (SedimentStructureItem*) item(r);
        if (ret->getSedimentStructure()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void SedimentStructureInBedItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        SedimentStructureItem* itm = (SedimentStructureItem*) itemFromIndex(*it);
        _bed->removeSedimentStructure(itm->getSedimentStructure());
    }
    reload();
}

QModelIndex SedimentStructureInBedItemModel::findIndexForSedimentStructure(SedimentStructure* q) {
    if (!q) {
        return QModelIndex();
    }

    SedimentStructureItem* itm = findItemForSedimentStructure(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
