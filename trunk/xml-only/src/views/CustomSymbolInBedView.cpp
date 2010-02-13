/*
 * File:   CustomSymbolInBedView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "CustomSymbolInBedView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "CustomSymbolInBedItemModel.h"
#include "CustomSymbolItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "CustomSymbol.h"
#include "Bed.h"
#include "BedEditorDialog.h"

CustomSymbolInBedView::CustomSymbolInBedView(QWidget* p, CustomSymbolInBedItemModel* model)
: TreeView(p),
_bed(0) {
    setModel(model);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    setContextMenuPolicy(Qt::CustomContextMenu);

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));

    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDeleteRequested(QModelIndexList)));
}

CustomSymbolInBedView::~CustomSymbolInBedView() {
}

void CustomSymbolInBedView::slotCurrentBedChanged(Bed* b) {
    _bed = b;
    setEnabled(_bed);
}

void CustomSymbolInBedView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* deleteA = new QAction(tr("Remove From Bed"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(deleteA, SIGNAL(activated()), this, SLOT(slotDelete()));

    if (selectedIndexes().count() > 0) {
        m->addAction(deleteA);
    }
    m->insertSeparator(reloadA);
    m->addAction(reloadA);
    m->exec(mapToGlobal(p));
}

void CustomSymbolInBedView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void CustomSymbolInBedView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        CustomSymbolItem* itm = (CustomSymbolItem*) ((CustomSymbolInBedItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getCustomSymbol()->getName();
        }
    }

    emit deleteRequest(selected);
}

void CustomSymbolInBedView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentCustomSymbolChanged(0);
        return;
    }

    CustomSymbolItem* itm = (CustomSymbolItem*) (((CustomSymbolInBedItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentCustomSymbolChanged(0);
    } else {
        emit currentCustomSymbolChanged(itm->getCustomSymbol());
    }
}

void CustomSymbolInBedView::slotReload() {
    emit currentCustomSymbolChanged(0);
    emit reloadRequest();
}

void CustomSymbolInBedView::selectCustomSymbol(CustomSymbol* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((CustomSymbolInBedItemModel*)model())->findIndexForCustomSymbol(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}


QList<CustomSymbol*> CustomSymbolInBedView::getSelectedCustomSymbols() {
    QList<CustomSymbol*> ret;

    QModelIndexList selected = selectedIndexes();

    for (QModelIndexList::iterator it = selected.begin(); it != selected.end(); it++) {
        CustomSymbolItem* itm = (CustomSymbolItem*) ((CustomSymbolInBedItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            ret.append(itm->getCustomSymbol());
        }
    }

    return ret;
}
