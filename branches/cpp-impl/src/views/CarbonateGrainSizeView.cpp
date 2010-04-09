/*
 * File:   CarbonateGrainSizeView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "CarbonateGrainSizeView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "CarbonateGrainSizeItemModel.h"
#include "CarbonateGrainSizeItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "CarbonateGrainSize.h"

CarbonateGrainSizeView::CarbonateGrainSizeView(QWidget* p, CarbonateGrainSizeItemModel* model)
: GrainSizeView(p),
_project(0) {
    setModel(model);
    setContextMenuPolicy(Qt::CustomContextMenu);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));
    
    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect((static_cast<ProfileLogger*> (QApplication::instance())), SIGNAL(currentProjectChanged(Project*)), this, SLOT(slotCurrentProjectChanged(Project*)));
    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));

    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
}

CarbonateGrainSizeView::~CarbonateGrainSizeView() {
}

void CarbonateGrainSizeView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void CarbonateGrainSizeView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));

    m->addAction(reloadA);
    m->exec(mapToGlobal(p));
}

void CarbonateGrainSizeView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void CarbonateGrainSizeView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentCarbonateGrainSizeChanged(0);
        return;
    }

    CarbonateGrainSizeItem* itm = (CarbonateGrainSizeItem*) (((CarbonateGrainSizeItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentCarbonateGrainSizeChanged(0);
    } else {
        emit currentCarbonateGrainSizeChanged(itm->getCarbonateGrainSize());
    }
}

void CarbonateGrainSizeView::slotReload() {
    emit currentCarbonateGrainSizeChanged(0);
    emit reloadRequest();
}

void CarbonateGrainSizeView::selectCarbonateGrainSize(CarbonateGrainSize* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((CarbonateGrainSizeItemModel*)model())->findIndexForCarbonateGrainSize(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
