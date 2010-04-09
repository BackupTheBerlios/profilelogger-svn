/*
 * File:   BoundaryTypeView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "BoundaryTypeView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "BoundaryTypeItemModel.h"
#include "BoundaryTypeItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "BoundaryType.h"
#include "Bed.h"
#include "BedEditorDialog.h"
#include "ManagementToolBox.h"

BoundaryTypeView::BoundaryTypeView(QWidget* p, BoundaryTypeItemModel* model)
: TreeView(p),
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
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEditRequested(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDeleteRequested(QModelIndexList)));
}

BoundaryTypeView::~BoundaryTypeView() {
}

void BoundaryTypeView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void BoundaryTypeView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (BoundaryTypeItemModel*) model(), SLOT(createNew()));
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

void BoundaryTypeView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void BoundaryTypeView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void BoundaryTypeView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        BoundaryTypeItem* itm = (BoundaryTypeItem*) ((BoundaryTypeItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getBoundaryType()->getName();
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

void BoundaryTypeView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentBoundaryTypeChanged(0);
        return;
    }

    BoundaryTypeItem* itm = (BoundaryTypeItem*) (((BoundaryTypeItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentBoundaryTypeChanged(0);
    } else {
        emit currentBoundaryTypeChanged(itm->getBoundaryType());
    }
}

void BoundaryTypeView::slotReload() {
    emit currentBoundaryTypeChanged(0);
    emit reloadRequest();
}

void BoundaryTypeView::selectBoundaryType(BoundaryType* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((BoundaryTypeItemModel*)model())->findIndexForBoundaryType(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
