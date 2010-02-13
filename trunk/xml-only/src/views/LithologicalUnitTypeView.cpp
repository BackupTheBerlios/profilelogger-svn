/*
 * File:   LithologicalUnitTypeView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "LithologicalUnitTypeView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "LithologicalUnitTypeItemModel.h"
#include "LithologicalUnitTypeItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "LithologicalUnitType.h"
#include "Bed.h"
#include "BedEditorDialog.h"

LithologicalUnitTypeView::LithologicalUnitTypeView(QWidget* p, LithologicalUnitTypeItemModel* model)
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

LithologicalUnitTypeView::~LithologicalUnitTypeView() {
}

void LithologicalUnitTypeView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void LithologicalUnitTypeView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (LithologicalUnitTypeItemModel*) model(), SLOT(createNew()));
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

void LithologicalUnitTypeView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void LithologicalUnitTypeView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void LithologicalUnitTypeView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        LithologicalUnitTypeItem* itm = (LithologicalUnitTypeItem*) ((LithologicalUnitTypeItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getLithologicalUnitType()->getName();
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

void LithologicalUnitTypeView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentLithologicalUnitTypeChanged(0);
        return;
    }

    LithologicalUnitTypeItem* itm = (LithologicalUnitTypeItem*) (((LithologicalUnitTypeItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentLithologicalUnitTypeChanged(0);
    } else {
        emit currentLithologicalUnitTypeChanged(itm->getLithologicalUnitType());
    }
}

void LithologicalUnitTypeView::slotReload() {
    emit currentLithologicalUnitTypeChanged(0);
    emit reloadRequest();
}

void LithologicalUnitTypeView::selectLithologicalUnitType(LithologicalUnitType* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((LithologicalUnitTypeItemModel*)model())->findIndexForLithologicalUnitType(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
