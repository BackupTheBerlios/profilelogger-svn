/* 
 * File:   BedItemView.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 11:40
 */

#include "BedItemView.h"

#include <QMenu>
#include <QAction>
#include <QMessageBox>

#include "MainWindow.h"
#include "Profile.h"
#include "BedItemModel.h"
#include "WorkWidget.h"
#include "Bed.h"
#include "BedItem.h"

BedItemView::BedItemView(QWidget* p, BedItemModel* model)
: TreeView(p),
_profile(0) {
    // setSortingEnabled(true);
    setEnabled(false);

    setModel(model);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    setContextMenuPolicy(Qt::CustomContextMenu);

    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(model, SIGNAL(selectRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));
    connect(this, SIGNAL(createBedOnTopRequest()), model, SLOT(slotCreateBedOnTop()));
    connect(this, SIGNAL(createBedAboveRequest(const QModelIndex&)), model, SLOT(slotCreateBedAbove(const QModelIndex&)));
    connect(this, SIGNAL(createBedBelowRequest(const QModelIndex&)), model, SLOT(slotCreateBedBelow(const QModelIndex&)));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEdit(const QModelIndex&)));
    connect(this, SIGNAL(moveUpRequest(const QModelIndex&)), model, SLOT(slotMoveUp(const QModelIndex&)));
    connect(this, SIGNAL(moveDownRequest(const QModelIndex&)), model, SLOT(slotMoveDown(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDelete(QModelIndexList)));
    connect(this, SIGNAL(duplicateAndInsertOnTopRequest(const QModelIndex&)), model, SLOT(slotDuplicateAndInsertOnTop(const QModelIndex&)));
    connect(this, SIGNAL(splitProfileAtRequest(const QModelIndex&)), model, SLOT(slotSplitProfileAt(const QModelIndex&)));
    connect(this, SIGNAL(deleteBedsAboveRequest(const QModelIndex&)), model, SLOT(slotDeleteBedsAbove(const QModelIndex&)));
    connect(this, SIGNAL(deleteBedsBelowRequest(const QModelIndex&)), model, SLOT(slotDeleteBedsBelow(const QModelIndex&)));
}

BedItemView::~BedItemView() {
}

void BedItemView::slotCurrentProfileChanged(Profile* p) {
    _profile = p;
    setEnabled(0 != _profile);
    emit currentBedChanged(0);
}

void BedItemView::slotCustomContextMenuRequested(const QPoint& p) {
    ProfileLogger* app = (static_cast<ProfileLogger*>(QApplication::instance()));
    
    QMenu* m = new QMenu((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow());

    m->addAction(app->getReloadBedsAction());
    m->insertSeparator(app->getCreateBedOnTopAction());
    m->addAction(app->getCreateBedOnTopAction());
    m->addAction(app->getCreateBedAboveCurrentBedAction());
    m->addAction(app->getCreateBedBelowCurrentBedAction());
    m->insertSeparator(app->getEditBedAction());
    m->addAction(app->getEditBedAction());
    m->addAction(app->getMoveBedUpAction());
    m->addAction(app->getMoveBedDownAction());
    m->addAction(app->getDuplicateBedAndInsertAtTopAction());
    m->insertSeparator(app->getSplitProfileAtBedAction());
    m->addAction(app->getSplitProfileAtBedAction());
    m->addAction(app->getInsertProfileAboveBedAction());
    //m->addAction(app->getInsertProfileBelowBedAction());
    m->insertSeparator(app->getDeleteBedAction());
    m->addAction(app->getDeleteBedAction());
    m->addAction(app->getDeleteBedsAboveBedAction());
    m->addAction(app->getDeleteBedsBelowBelowAction());

    m->insertSeparator(app->getExportProfileToSvgAction());
    m->addAction(app->getExportProfileToSvgAction());
    m->addAction(app->getExportProfileToPdfAction());
    m->addAction(app->getExportProfileToJpgAction());
    m->addAction(app->getExportProfileToPngAction());
    m->addAction(app->getExportProfileToTiffAction());

    m->exec(mapToGlobal(p));
}

void BedItemView::slotReload() {
    emit currentBedChanged(0);
    emit reloadRequest();
    sortByColumn(0, Qt::DescendingOrder);
}

void BedItemView::slotCreateNewOnTop() {
    emit createBedOnTopRequest();
}

void BedItemView::slotCreateAboveCurrent() {
    QModelIndex idx = currentIndex();
    if (!idx.isValid()) {
        return;
    }
    emit createBedAboveRequest(idx);
}

void BedItemView::slotCreateBelowCurrent() {
    QModelIndex idx = currentIndex();
    if (!idx.isValid()) {
        return;
    }
    emit createBedBelowRequest(idx);
}

void BedItemView::slotMoveUp() {
    QModelIndex idx = currentIndex();
    if (!idx.isValid()) {
        return;
    }

    emit moveUpRequest(idx);
}

void BedItemView::slotMoveDown() {
    QModelIndex idx = currentIndex();
    if (!idx.isValid()) {
        return;
    }

    emit moveDownRequest(idx);
}

void BedItemView::slotEdit() {
    QModelIndex idx = currentIndex();
    if (!idx.isValid()) {
        return;
    }

    emit editRequest(idx);
}

void BedItemView::slotSplitProfileHere() {
    QModelIndex idx = currentIndex();

    if (!idx.isValid()) {
        return;
    }

    BedItem* itm = (BedItem*) ((BedItemModel*) model())->itemFromIndex(idx);

    if (QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), tr("Split Profile?"),
            tr("Split Profile above bed %1?").arg(itm->getBed()->getName()),
            QMessageBox::Yes | QMessageBox::No) != QMessageBox::Yes) {
        return;
    }

    emit splitProfileAtRequest(idx);
}

void BedItemView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    if (selected.isEmpty()) {
        return;
    }

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin(); it != selected.end(); it++) {
        BedItem* itm = (BedItem*) ((BedItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << tr("Position: %1, ID: %2")
                    .arg(itm->getBed()->getPosition())
                    .arg(itm->getBed()->getId());
        }
    }

    if (QMessageBox::Yes == QMessageBox::warning(this,
            tr("Really Delete?"),
            tr("Really delete this Beds?\n%1")
            .arg(names.join(", ")),
            QMessageBox::Yes | QMessageBox::No)) {
        emit deleteRequest(selected);
    }
}

void BedItemView::slotDeleteBedsAboveCurrentBed() {
    QModelIndex idx = currentIndex();

    if (!idx.isValid()) {
        return;
    }

    BedItem* itm = (BedItem*) ((BedItemModel*) model())->itemFromIndex(idx);

    if (QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), tr("Split Profile?"),
            tr("Delete all beds above bed %1?").arg(itm->getBed()->getName()),
            QMessageBox::Yes | QMessageBox::No) != QMessageBox::Yes) {
        return;
    }

    emit deleteBedsAboveRequest(idx);
}

void BedItemView::slotDeleteBedsBelowCurrentBed() {
    QModelIndex idx = currentIndex();

    if (!idx.isValid()) {
        return;
    }

    BedItem* itm = (BedItem*) ((BedItemModel*) model())->itemFromIndex(idx);

    if (QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), tr("Split Profile?"),
            tr("Delete all beds below bed %1?").arg(itm->getBed()->getName()),
            QMessageBox::Yes | QMessageBox::No) != QMessageBox::Yes) {
        return;
    }

    emit deleteBedsAboveRequest(idx);
}

void BedItemView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentBedChanged(0);
        return;
    }

    BedItem* itm = (BedItem*) (((BedItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentBedChanged(0);
    } else {
        emit currentBedChanged(itm->getBed());
    }
}

void BedItemView::slotReloaded() {
    sortByColumn(1, Qt::DescendingOrder);
}

void BedItemView::slotDuplicateAndInsertOnTop() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    QModelIndex idx = selected.first();
    BedItem* itm = (BedItem*) ((BedItemModel*) model())->itemFromIndex(idx);

    if (!itm) {
        return;
    }

    if (QMessageBox::Yes == QMessageBox::question(this,
            tr("Duplicate and insert on top?"),
            tr("Really duplicate bed <b>%1</b> and insert on top?")
            .arg(QString::number(itm->getBed()->getPosition())),
            QMessageBox::Yes | QMessageBox::No)) {
        emit duplicateAndInsertOnTopRequest(idx);
    }
}

void BedItemView::selectBed(Bed* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((BedItemModel*)model())->findIndexForBed(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}

void BedItemView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}
