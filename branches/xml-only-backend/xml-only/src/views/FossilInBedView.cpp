/*
 * File:   FossilInBedView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "FossilInBedView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "FossilInBedItemModel.h"
#include "FossilItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "Fossil.h"
#include "Bed.h"
#include "BedEditorDialog.h"

FossilInBedView::FossilInBedView(QWidget* p, FossilInBedItemModel* model)
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

FossilInBedView::~FossilInBedView() {
}

void FossilInBedView::slotCurrentBedChanged(Bed* b) {
    _bed = b;
    setEnabled(_bed);
}

void FossilInBedView::slotCustomContextMenuRequested(const QPoint& p) {
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

void FossilInBedView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void FossilInBedView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        FossilItem* itm = (FossilItem*) ((FossilInBedItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getFossil()->getName();
        }
    }

    emit deleteRequest(selected);
}

void FossilInBedView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentFossilChanged(0);
        return;
    }

    FossilItem* itm = (FossilItem*) (((FossilInBedItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentFossilChanged(0);
    } else {
        emit currentFossilChanged(itm->getFossil());
    }
}

void FossilInBedView::slotReload() {
    emit currentFossilChanged(0);
    emit reloadRequest();
}

void FossilInBedView::selectFossil(Fossil* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((FossilInBedItemModel*)model())->findIndexForFossil(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}


QList<Fossil*> FossilInBedView::getSelectedFossils() {
    QList<Fossil*> ret;

    QModelIndexList selected = selectedIndexes();

    for (QModelIndexList::iterator it = selected.begin(); it != selected.end(); it++) {
        FossilItem* itm = (FossilItem*) ((FossilInBedItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            ret.append(itm->getFossil());
        }
    }

    return ret;
}
