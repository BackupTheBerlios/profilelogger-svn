/* 
 * File:   OutcropQualityView.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 16:44
 */

#include "OutcropQualityView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "OutcropQualityItemModel.h"
#include "OutcropQualityItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "OutcropQuality.h"
#include "Bed.h"
#include "BedEditorDialog.h"

OutcropQualityView::OutcropQualityView(QWidget* p, OutcropQualityItemModel* model)
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

OutcropQualityView::~OutcropQualityView() {
}

void OutcropQualityView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void OutcropQualityView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (OutcropQualityItemModel*) model(), SLOT(createNew()));
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

void OutcropQualityView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void OutcropQualityView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void OutcropQualityView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        OutcropQualityItem* itm = (OutcropQualityItem*) ((OutcropQualityItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getOutcropQuality()->getName();
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

void OutcropQualityView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentOutcropQualityChanged(0);
        return;
    }

    OutcropQualityItem* itm = (OutcropQualityItem*) (((OutcropQualityItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentOutcropQualityChanged(0);
    } else {
        emit currentOutcropQualityChanged(itm->getOutcropQuality());
    }
}

void OutcropQualityView::slotReload() {
    emit currentOutcropQualityChanged(0);
    emit reloadRequest();
}

void OutcropQualityView::selectOutcropQuality(OutcropQuality* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }
   
    QModelIndex idx = ((OutcropQualityItemModel*)model())->findIndexForOutcropQuality(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
