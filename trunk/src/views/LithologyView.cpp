/*
 * File:   LithologyView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "LithologyView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "LithologyItemModel.h"
#include "LithologyItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "Lithology.h"
#include "Bed.h"
#include "BedEditorDialog.h"

LithologyView::LithologyView(QWidget* p, LithologyItemModel* model)
: TreeView(p),
_project(0) {
    setModel(model);
    setSortingEnabled(true);

    setContextMenuPolicy(Qt::CustomContextMenu);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect(static_cast<ProfileLogger*> (QApplication::instance()), SIGNAL(currentProjectChanged(Project*)), this, SLOT(slotCurrentProjectChanged(Project*)));
    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));

    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEditRequested(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDeleteRequested(QModelIndexList)));
}

LithologyView::~LithologyView() {
}

void LithologyView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void LithologyView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (LithologyItemModel*) model(), SLOT(createNew()));
    connect(editA, SIGNAL(activated()), this, SLOT(slotEdit()));
    connect(deleteA, SIGNAL(activated()), this, SLOT(slotDelete()));

    m->addAction(createA);
    if (selectedIndexes().count() == 1) {
        m->addAction(editA);
    }
    if (selectedIndexes().count() > 0) {
        m->addAction(deleteA);
    }
    m->insertSeparator(reloadA);
    m->addAction(reloadA);
    m->exec(mapToGlobal(p));
}

void LithologyView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void LithologyView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void LithologyView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        LithologyItem* itm = (LithologyItem*) ((LithologyItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getLithology()->getName();
        }
    }

    if (QMessageBox::Yes == QMessageBox::warning(this,
            tr("Really Delete?"),
            tr("Really delete this Datasets?\n%1")
            .arg(names.join(", ")),
            QMessageBox::Yes | QMessageBox::No)) {
        emit deleteRequest(selected);
    }
}

void LithologyView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentLithologyChanged(0);
        return;
    }

    LithologyItem* itm = (LithologyItem*) (((LithologyItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentLithologyChanged(0);
    } else {
        emit currentLithologyChanged(itm->getLithology());
    }
}

void LithologyView::slotReload() {
    emit currentLithologyChanged(0);
    emit reloadRequest();
}

void LithologyView::selectLithology(Lithology* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((LithologyItemModel*) model())->findIndexForLithology(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}

void LithologyView::slotReloaded() {
    sortByColumn(0, Qt::AscendingOrder);
}
