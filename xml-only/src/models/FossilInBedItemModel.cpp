/*
 * File:   FossilInBedItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "FossilInBedItemModel.h"

#include <QApplication>
#include <QMimeData>

#include "ProfileLogger.h"
#include "FossilItem.h"
#include "Project.h"
#include "Bed.h"
#include "FossilEditorDialog.h"
#include "Fossil.h"

class Project;

FossilInBedItemModel::FossilInBedItemModel(QObject* p)
: StandardItemModel(p),
_bed(0) {
}

FossilInBedItemModel::~FossilInBedItemModel() {
}

void FossilInBedItemModel::slotCurrentBedChanged(Bed* b) {
    _bed = b;
    reload();
}

void FossilInBedItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Fossil");
    setHorizontalHeaderLabels(hh);

    if (!_bed) {
        return;
    }

    QList<Fossil*>::iterator it = _bed->getFirstFossil();
    QList<Fossil*>::iterator last = _bed->getLastFossil();

    while (it != last) {
        Fossil* f = *it;
        if (f) {
            appendItem(*it);
        }
        it++;
    }

    emit reloaded();
}

FossilItem* FossilInBedItemModel::appendItem(Fossil* p) {
    FossilItem* i = new FossilItem(p);
    appendRow(i);
    return i;
}

FossilItem* FossilInBedItemModel::findItemForFossil(int id) {
    for (int r = 0; r < rowCount(); r++) {
        FossilItem* ret = (FossilItem*) item(r);
        if (ret->getFossil()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void FossilInBedItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        FossilItem* itm = (FossilItem*) itemFromIndex(*it);
        _bed->removeFossil(itm->getFossil());
    }
    reload();
}

QModelIndex FossilInBedItemModel::findIndexForFossil(Fossil* q) {
    if (!q) {
        return QModelIndex();
    }

    FossilItem* itm = findItemForFossil(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
