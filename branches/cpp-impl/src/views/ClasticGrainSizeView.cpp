/*
 * File:   ClasticGrainSizeView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "ClasticGrainSizeView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "ClasticGrainSizeItemModel.h"
#include "ClasticGrainSizeItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "ClasticGrainSize.h"

ClasticGrainSizeView::ClasticGrainSizeView(QWidget* p, ClasticGrainSizeItemModel* model)
: GrainSizeView(p),
_project(0) {
    setModel(model);
    setContextMenuPolicy(Qt::CustomContextMenu);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect(static_cast<ProfileLogger*> (QApplication::instance()), SIGNAL(currentProjectChanged(Project*)), this, SLOT(slotCurrentProjectChanged(Project*)));
    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));

    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
}

ClasticGrainSizeView::~ClasticGrainSizeView() {
}

void ClasticGrainSizeView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void ClasticGrainSizeView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));

    m->addAction(reloadA);
    m->exec(mapToGlobal(p));
}

void ClasticGrainSizeView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void ClasticGrainSizeView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentClasticGrainSizeChanged(0);
        return;
    }

    ClasticGrainSizeItem* itm = (ClasticGrainSizeItem*) (((ClasticGrainSizeItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentClasticGrainSizeChanged(0);
    } else {
        emit currentClasticGrainSizeChanged(itm->getClasticGrainSize());
    }
}

void ClasticGrainSizeView::slotReload() {
    emit currentClasticGrainSizeChanged(0);
    emit reloadRequest();
}

void ClasticGrainSizeView::selectClasticGrainSize(ClasticGrainSize* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((ClasticGrainSizeItemModel*)model())->findIndexForClasticGrainSize(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
