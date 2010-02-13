/* 
 * File:   ProfileItemView.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:13
 */

#include "ProfileItemView.h"

#include <QMenu>
#include <QAction>
#include <QMessageBox>
#include <QFileDialog>
#include <qabstractitemmodel.h>

#include "ProfileItemModel.h"
#include "ProfileLogger.h"
#include "WorkWidget.h"
#include "ProfileItem.h"
#include "Dataset.h"
#include "Profile.h"
#include "CsvProfileImportSettingsDialog.h"
#include "CsvProfileImportSettings.h"

ProfileItemView::ProfileItemView(QWidget* p, ProfileItemModel* model)
: TreeView(p),
_project(0) {
    setModel(model);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    setContextMenuPolicy(Qt::CustomContextMenu);

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    connect((static_cast<ProfileLogger*> (QApplication::instance())), SIGNAL(currentProjectChanged(Project*)), this, SLOT(slotCurrentProjectChanged(Project*)));
    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));
    connect(this, SIGNAL(importFromCsvFileRequest(const QModelIndex&)), model, SLOT(slotImportFromCsvFileRequested(const QModelIndex&)));
    
    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEditRequested(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDeleteRequested(QModelIndexList)));
    connect(this, SIGNAL(duplicateRequest(const QModelIndex&)), model, SLOT(slotDuplicateRequested(const QModelIndex&)));
    setEnabled(false);
}

ProfileItemView::~ProfileItemView() {
}

void ProfileItemView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);
    QAction* duplicateA = new QAction(tr("Duplicate"), this);
    QAction* importA = new QAction(tr("Import from CSV File..."), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (ProfileItemModel*) model(), SLOT(createNew()));
    connect(editA, SIGNAL(activated()), this, SLOT(slotEdit()));
    connect(deleteA, SIGNAL(activated()), this, SLOT(slotDelete()));
    connect(duplicateA, SIGNAL(activated()), this, SLOT(slotDuplicate()));
    connect(importA, SIGNAL(activated()), this, SLOT(slotImportFromCsvFile()));
    
    m->addAction(createA);
    if (selectedIndexes().count() == 1) {
        m->addAction(editA);
        m->addAction(duplicateA);
    }
    if (selectedIndexes().count() > 0) {
        m->addAction(deleteA);
    }
    m->insertSeparator(reloadA);
    m->addAction(reloadA);
    m->insertSeparator(importA);
    m->addAction(importA);
    m->exec(mapToGlobal(p));
}

void ProfileItemView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void ProfileItemView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void ProfileItemView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void ProfileItemView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        ProfileItem* itm = (ProfileItem*) ((ProfileItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getProfile()->getName();
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

void ProfileItemView::slotIndexActivated(const QModelIndex& idx) {
    ProfileItem* itm = (ProfileItem*) (((ProfileItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentProfileChanged(0);
    } else {
        emit currentProfileChanged(itm->getProfile());
    }
}

void ProfileItemView::slotReload() {
    emit currentProfileChanged(0);
    emit reloadRequest();
}

void ProfileItemView::slotDuplicate() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit duplicateRequest(selected.first());
}

void ProfileItemView::slotImportFromCsvFile() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit importFromCsvFileRequest(selected.first());
}

void ProfileItemView::selectProfile(Profile* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((ProfileItemModel*)model())->findIndexForProfile(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
