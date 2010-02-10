/*
 * File:   SampleItemView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:40
 */

#include "SampleItemView.h"

#include <QMenu>
#include <QAction>
#include <QMessageBox>

#include "Profile.h"
#include "SampleItemModel.h"
#include "WorkWidget.h"
#include "Sample.h"
#include "SampleItem.h"

SampleItemView::SampleItemView(QWidget* p, SampleItemModel* model)
: TreeView(p),
_profile(0) {
    // setSortingEnabled(true);
    setEnabled(false);

    setModel(model);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    setContextMenuPolicy(Qt::CustomContextMenu);

    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));
    connect(this, SIGNAL(createSampleRequest()), model, SLOT(slotCreate()));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEdit(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDelete(QModelIndexList)));
    connect(this, SIGNAL(exportToLatexRequest()), model, SLOT(slotExportToLatex()));
}

SampleItemView::~SampleItemView() {
}

void SampleItemView::slotCurrentProfileChanged(Profile* p) {
    _profile = p;
    setEnabled(_profile);
    emit currentSampleChanged(0);
}

void SampleItemView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create Sample..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);
    QAction* exportA = new QAction(tr("Export as LaTeX table..."), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), this, SLOT(slotCreate()));
    connect(editA, SIGNAL(activated()), this, SLOT(slotEdit()));
    connect(deleteA, SIGNAL(activated()), this, SLOT(slotDelete()));
    connect(exportA, SIGNAL(activated()), this, SLOT(slotExportToLatex()));

    m->addAction(createA);

    if (selectedIndexes().count() == 1) {
        m->insertSeparator(editA);
        m->addAction(editA);
    }

    if (selectedIndexes().count() > 0) {
        m->insertSeparator(deleteA);
        m->addAction(deleteA);
    }
    m->addAction(reloadA);
    m->insertSeparator(exportA);
    m->addAction(exportA);
    m->exec(mapToGlobal(p));
}

void SampleItemView::slotReload() {
    emit currentSampleChanged(0);
    emit reloadRequest();
    sortByColumn(0, Qt::DescendingOrder);
}

void SampleItemView::slotCreate() {
    emit createSampleRequest();
}

void SampleItemView::slotEdit() {
    QModelIndex idx = currentIndex();
    if (!idx.isValid()) {
        return;
    }

    emit editRequest(idx);
}

void SampleItemView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    if (selected.isEmpty()) {
        return;
    }

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin(); it != selected.end(); it++) {
        SampleItem* itm = (SampleItem*) ((SampleItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << tr("Name: %1, ID: %2")
                    .arg(itm->getSample()->getName())
                    .arg(itm->getSample()->getId());
        }
    }

    if (QMessageBox::Yes == QMessageBox::warning(this,
            tr("Really Delete?"),
            tr("Really delete this Samples?\n%1")
            .arg(names.join(", ")),
            QMessageBox::Yes | QMessageBox::No)) {
        emit deleteRequest(selected);
    }
}

void SampleItemView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentSampleChanged(0);
        return;
    }

    SampleItem* itm = (SampleItem*) (((SampleItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentSampleChanged(0);
    } else {
        emit currentSampleChanged(itm->getSample());
    }
}

void SampleItemView::slotReloaded() {
    sortByColumn(1, Qt::DescendingOrder);
}

void SampleItemView::slotExportToLatex() {
    emit exportToLatexRequest();
}
