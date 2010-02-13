/*
 * File:   CustomSymbolView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "CustomSymbolView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "CustomSymbolItemModel.h"
#include "CustomSymbolItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "CustomSymbol.h"
#include "Bed.h"
#include "BedEditorDialog.h"

CustomSymbolView::CustomSymbolView(QWidget* p, CustomSymbolItemModel* model)
: TreeView(p),
_project(0) {
    setModel(model);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    setContextMenuPolicy(Qt::CustomContextMenu);

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), 
	    this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect(static_cast<ProfileLogger*> (QApplication::instance()), SIGNAL(currentProjectChanged(Project*)), 
	    this, SLOT(slotCurrentProjectChanged(Project*)));
    connect(this, SIGNAL(activated(const QModelIndex&)), 
	    this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));

    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEditRequested(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDeleteRequested(QModelIndexList)));
}

CustomSymbolView::~CustomSymbolView() {
}

void CustomSymbolView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void CustomSymbolView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (CustomSymbolItemModel*) model(), SLOT(createNew()));
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

void CustomSymbolView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void CustomSymbolView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void CustomSymbolView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        CustomSymbolItem* itm = (CustomSymbolItem*) ((CustomSymbolItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getCustomSymbol()->getName();
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

void CustomSymbolView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentCustomSymbolChanged(0);
        return;
    }

    CustomSymbolItem* itm = (CustomSymbolItem*) (((CustomSymbolItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentCustomSymbolChanged(0);
    } else {
        emit currentCustomSymbolChanged(itm->getCustomSymbol());
    }
}

void CustomSymbolView::slotReload() {
    emit currentCustomSymbolChanged(0);
    emit reloadRequest();
}

void CustomSymbolView::selectCustomSymbol(CustomSymbol* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((CustomSymbolItemModel*)model())->findIndexForCustomSymbol(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}

QList<CustomSymbol*> CustomSymbolView::getSelectedCustomSymbols() {
    QList<CustomSymbol*> ret;

    QModelIndexList selected = selectedIndexes();

    for (QModelIndexList::iterator it = selected.begin(); it != selected.end(); it++) {
        CustomSymbolItem* itm = (CustomSymbolItem*) ((CustomSymbolItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            ret.append(itm->getCustomSymbol());
        }
    }

    return ret;
}
