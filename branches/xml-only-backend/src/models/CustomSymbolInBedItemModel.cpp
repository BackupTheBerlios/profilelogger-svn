/*
 * File:   CustomSymbolInBedItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "CustomSymbolInBedItemModel.h"

#include <QApplication>
#include <QMimeData>

#include "ProfileLogger.h"
#include "CustomSymbolItem.h"
#include "Project.h"
#include "Bed.h"
#include "CustomSymbolEditorDialog.h"
#include "CustomSymbol.h"

class Project;

CustomSymbolInBedItemModel::CustomSymbolInBedItemModel(QObject* p)
: StandardItemModel(p),
_bed(0) {
}

CustomSymbolInBedItemModel::~CustomSymbolInBedItemModel() {
}

void CustomSymbolInBedItemModel::slotCurrentBedChanged(Bed* b) {
    _bed = b;
    reload();
}

void CustomSymbolInBedItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Custom Symbol");
    setHorizontalHeaderLabels(hh);

    if (!_bed) {
        return;
    }

    QList<CustomSymbol*>::iterator it = _bed->getFirstCustomSymbol();
    QList<CustomSymbol*>::iterator last = _bed->getLastCustomSymbol();

    while (it != last) {
        CustomSymbol* f = *it;
        if (f) {
            appendItem(*it);
        }
        it++;
    }

    emit reloaded();
}

CustomSymbolItem* CustomSymbolInBedItemModel::appendItem(CustomSymbol* p) {
    CustomSymbolItem* i = new CustomSymbolItem(p);
    appendRow(i);
    return i;
}

CustomSymbolItem* CustomSymbolInBedItemModel::findItemForCustomSymbol(int id) {
    for (int r = 0; r < rowCount(); r++) {
        CustomSymbolItem* ret = (CustomSymbolItem*) item(r);
        if (ret->getCustomSymbol()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void CustomSymbolInBedItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        CustomSymbolItem* itm = (CustomSymbolItem*) itemFromIndex(*it);
        _bed->removeCustomSymbol(itm->getCustomSymbol());
    }
    reload();
}

QModelIndex CustomSymbolInBedItemModel::findIndexForCustomSymbol(CustomSymbol* q) {
    if (!q) {
        return QModelIndex();
    }

    CustomSymbolItem* itm = findItemForCustomSymbol(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
