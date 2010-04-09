/*
 * File:   SedimentStructureInBedView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "SedimentStructureInBedView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "SedimentStructureInBedItemModel.h"
#include "SedimentStructureItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "SedimentStructure.h"
#include "Bed.h"
#include "BedEditorDialog.h"

SedimentStructureInBedView::SedimentStructureInBedView(QWidget* p, SedimentStructureInBedItemModel* model)
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

SedimentStructureInBedView::~SedimentStructureInBedView() {
}

void SedimentStructureInBedView::slotCurrentBedChanged(Bed* b) {
    _bed = b;
    setEnabled(_bed);
}

void SedimentStructureInBedView::slotCustomContextMenuRequested(const QPoint& p) {
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

void SedimentStructureInBedView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void SedimentStructureInBedView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        SedimentStructureItem* itm = (SedimentStructureItem*) ((SedimentStructureInBedItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getSedimentStructure()->getName();
        }
    }

    emit deleteRequest(selected);
}

void SedimentStructureInBedView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentSedimentStructureChanged(0);
        return;
    }

    SedimentStructureItem* itm = (SedimentStructureItem*) (((SedimentStructureInBedItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentSedimentStructureChanged(0);
    } else {
        emit currentSedimentStructureChanged(itm->getSedimentStructure());
    }
}

void SedimentStructureInBedView::slotReload() {
    emit currentSedimentStructureChanged(0);
    emit reloadRequest();
}

void SedimentStructureInBedView::selectSedimentStructure(SedimentStructure* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((SedimentStructureInBedItemModel*) model())->findIndexForSedimentStructure(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}

QList<SedimentStructure*> SedimentStructureInBedView::getSelectedSedimentStructures() {
    QList<SedimentStructure*> ret;

    QModelIndexList selected = selectedIndexes();

    for (QModelIndexList::iterator it = selected.begin(); it != selected.end(); it++) {
        SedimentStructureItem* itm = (SedimentStructureItem*) ((SedimentStructureInBedItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            ret.append(itm->getSedimentStructure());
        }
    }

    return ret;
}
