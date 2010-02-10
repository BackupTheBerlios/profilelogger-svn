/*
 * File:   ImageItemView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:40
 */

#include "ImageItemView.h"

#include <QMenu>
#include <QAction>
#include <QMessageBox>

#include "Profile.h"
#include "ImageItemModel.h"
#include "WorkWidget.h"
#include "Image.h"
#include "ImageItem.h"

ImageItemView::ImageItemView(QWidget* p, ImageItemModel* model)
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
    connect(this, SIGNAL(createImageRequest()), model, SLOT(slotCreate()));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEdit(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDelete(QModelIndexList)));
}

ImageItemView::~ImageItemView() {
}

void ImageItemView::slotCurrentProfileChanged(Profile* p) {
    _profile = p;
    setEnabled(_profile);
    emit currentImageChanged(0);
}

void ImageItemView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create Image..."), this);
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

void ImageItemView::slotReload() {
    emit currentImageChanged(0);
    emit reloadRequest();
    sortByColumn(0, Qt::DescendingOrder);
}

void ImageItemView::slotCreate() {
    emit createImageRequest();
}

void ImageItemView::slotEdit() {
    QModelIndex idx = currentIndex();
    if (!idx.isValid()) {
        return;
    }

    emit editRequest(idx);
}

void ImageItemView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    if (selected.isEmpty()) {
        return;
    }

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin(); it != selected.end(); it++) {
        ImageItem* itm = (ImageItem*) ((ImageItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << tr("Name: %1, ID: %2")
                    .arg(itm->getImage()->getName())
                    .arg(itm->getImage()->getId());
        }
    }

    if (QMessageBox::Yes == QMessageBox::warning(this,
            tr("Really Delete?"),
            tr("Really delete this Images?\n%1")
            .arg(names.join(", ")),
            QMessageBox::Yes | QMessageBox::No)) {
        emit deleteRequest(selected);
    }
}

void ImageItemView::slotIndexActivated(const QModelIndex& idx) {
    if (!idx.isValid()) {
        emit currentImageChanged(0);
        return;
    }

    ImageItem* itm = (ImageItem*) (((ImageItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentImageChanged(0);
    } else {
        emit currentImageChanged(itm->getImage());
    }
}

void ImageItemView::slotReloaded() {
    sortByColumn(1, Qt::DescendingOrder);
}
