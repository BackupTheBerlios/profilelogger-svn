/*
 * File:   BedCorrelationItemView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:40
 */

#include "BedCorrelationItemView.h"

#include <QMenu>
#include <QAction>
#include <QMessageBox>

#include "ProfileCorrelation.h"
#include "BedCorrelationItemModel.h"
#include "WorkWidget.h"
#include "BedCorrelation.h"
#include "BedCorrelationItem.h"

BedCorrelationItemView::BedCorrelationItemView(QWidget* p, BedCorrelationItemModel* model)
: TreeView(p),
_profileCorrelation(0) {
    // setSortingEnabled(true);
    setEnabled(false);

    setModel(model);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    setContextMenuPolicy(Qt::CustomContextMenu);

    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));
    connect(this, SIGNAL(createBedCorrelationRequest()), model, SLOT(slotCreate()));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEdit(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDelete(QModelIndexList)));
}

BedCorrelationItemView::~BedCorrelationItemView() {
}

void BedCorrelationItemView::slotCurrentProfileCorrelationChanged(ProfileCorrelation* p) {
    _profileCorrelation = p;
    setEnabled(_profileCorrelation);
    emit currentBedCorrelationChanged(0);
}

void BedCorrelationItemView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create BedCorrelation..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), this, SLOT(slotCreate()));
    connect(editA, SIGNAL(activated()), this, SLOT(slotEdit()));
    connect(deleteA, SIGNAL(activated()), this, SLOT(slotDelete()));

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
    m->exec(mapToGlobal(p));
}

void BedCorrelationItemView::slotReload() {
    emit currentBedCorrelationChanged(0);
    emit reloadRequest();
    sortByColumn(0, Qt::DescendingOrder);
}

void BedCorrelationItemView::slotCreate() {
    emit createBedCorrelationRequest();
}

void BedCorrelationItemView::slotEdit() {
    QModelIndex idx = currentIndex();
    if (!idx.isValid()) {
        return;
    }

    emit editRequest(idx);
}

void BedCorrelationItemView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    if (selected.isEmpty()) {
        return;
    }

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin(); it != selected.end(); it++) {
        BedCorrelationItem* itm = (BedCorrelationItem*) ((BedCorrelationItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << tr("Name: %1, ID: %2")
                    .arg(itm->getBedCorrelation()->getName())
                    .arg(itm->getBedCorrelation()->getId());
        }
    }

    if (QMessageBox::Yes == QMessageBox::warning(this,
            tr("Really Delete?"),
            tr("Really delete this BedCorrelations?\n%1")
            .arg(names.join(", ")),
            QMessageBox::Yes | QMessageBox::No)) {
        emit deleteRequest(selected);
    }
}

void BedCorrelationItemView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentBedCorrelationChanged(0);
        return;
    }

    BedCorrelationItem* itm = (BedCorrelationItem*) (((BedCorrelationItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentBedCorrelationChanged(0);
    } else {
        emit currentBedCorrelationChanged(itm->getBedCorrelation());
    }
}

void BedCorrelationItemView::slotReloaded() {
    sortByColumn(1, Qt::DescendingOrder);
}
