/*
 * File:   FaciesView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "FaciesView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "FaciesItemModel.h"
#include "FaciesItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "Facies.h"
#include "Bed.h"
#include "BedEditorDialog.h"
#include "ManagementToolBox.h"

FaciesView::FaciesView(QWidget* p, FaciesItemModel* model)
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

FaciesView::~FaciesView() {
}

void FaciesView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void FaciesView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (FaciesItemModel*) model(), SLOT(createNew()));
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

void FaciesView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void FaciesView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void FaciesView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        FaciesItem* itm = (FaciesItem*) ((FaciesItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getFacies()->getName();
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

void FaciesView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentFaciesChanged(0);
        return;
    }

    FaciesItem* itm = (FaciesItem*) (((FaciesItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentFaciesChanged(0);
    } else {
        emit currentFaciesChanged(itm->getFacies());
    }
}

void FaciesView::slotReload() {
    emit currentFaciesChanged(0);
    emit reloadRequest();
}

void FaciesView::selectFacies(Facies* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((FaciesItemModel*)model())->findIndexForFacies(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
