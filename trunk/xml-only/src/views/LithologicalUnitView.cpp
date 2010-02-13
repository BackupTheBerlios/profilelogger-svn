/*
 * File:   LithologicalUnitView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "LithologicalUnitView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "LithologicalUnitItemModel.h"
#include "LithologicalUnitItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "LithologicalUnit.h"
#include "Bed.h"
#include "BedEditorDialog.h"

LithologicalUnitView::LithologicalUnitView(QWidget* p, LithologicalUnitItemModel* model)
: TreeView(p),
_project(0) {
    setModel(model);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    setContextMenuPolicy(Qt::CustomContextMenu);

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect(static_cast<ProfileLogger*> (QApplication::instance()), SIGNAL(currentProjectChanged(Project*)), this, SLOT(slotCurrentProjectChanged(Project*)));
    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));

    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEditRequested(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDeleteRequested(QModelIndexList)));
}

LithologicalUnitView::~LithologicalUnitView() {
}

void LithologicalUnitView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void LithologicalUnitView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (LithologicalUnitItemModel*) model(), SLOT(createNew()));
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

void LithologicalUnitView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void LithologicalUnitView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void LithologicalUnitView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        LithologicalUnitItem* itm = (LithologicalUnitItem*) ((LithologicalUnitItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getLithologicalUnit()->getName();
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

void LithologicalUnitView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentLithologicalUnitChanged(0);
        return;
    }

    LithologicalUnitItem* itm = (LithologicalUnitItem*) (((LithologicalUnitItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentLithologicalUnitChanged(0);
    } else {
        emit currentLithologicalUnitChanged(itm->getLithologicalUnit());
    }
}

void LithologicalUnitView::slotReload() {
    emit currentLithologicalUnitChanged(0);
    emit reloadRequest();
}

void LithologicalUnitView::selectLithologicalUnit(LithologicalUnit* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((LithologicalUnitItemModel*)model())->findIndexForLithologicalUnit(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
