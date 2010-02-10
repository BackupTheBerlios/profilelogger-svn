/* 
 * File:   ProfileCorrelationItemView.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:13
 */

#include "ProfileCorrelationItemView.h"

#include <QMenu>
#include <QAction>
#include <QMessageBox>
#include <QFileDialog>

#include "ProfileCorrelationItemModel.h"
#include "ProfileLogger.h"
#include "WorkWidget.h"
#include "ProfileCorrelationItem.h"
#include "Dataset.h"
#include "ProfileCorrelation.h"

ProfileCorrelationItemView::ProfileCorrelationItemView(QWidget* p, ProfileCorrelationItemModel* model)
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
    
    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEditRequested(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDeleteRequested(QModelIndexList)));
    connect(this, SIGNAL(duplicateRequest(const QModelIndex&)), model, SLOT(slotDuplicateRequested(const QModelIndex&)));
    setEnabled(false);
}

ProfileCorrelationItemView::~ProfileCorrelationItemView() {
}

void ProfileCorrelationItemView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);
    QAction* duplicateA = new QAction(tr("Duplicate"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (ProfileCorrelationItemModel*) model(), SLOT(createNew()));
    connect(editA, SIGNAL(activated()), this, SLOT(slotEdit()));
    connect(deleteA, SIGNAL(activated()), this, SLOT(slotDelete()));
    connect(duplicateA, SIGNAL(activated()), this, SLOT(slotDuplicate()));
    
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
    m->exec(mapToGlobal(p));
}

void ProfileCorrelationItemView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}

void ProfileCorrelationItemView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void ProfileCorrelationItemView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void ProfileCorrelationItemView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        ProfileCorrelationItem* itm = (ProfileCorrelationItem*) ((ProfileCorrelationItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getProfileCorrelation()->getName();
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

void ProfileCorrelationItemView::slotIndexActivated(const QModelIndex& idx) {
    ProfileCorrelationItem* itm = (ProfileCorrelationItem*) (((ProfileCorrelationItemModel*) model())->itemFromIndex(idx));

    if (!itm) {
        emit currentProfileCorrelationChanged(0);
    } else {
        emit currentProfileCorrelationChanged(itm->getProfileCorrelation());
    }
}

void ProfileCorrelationItemView::slotReload() {
    emit currentProfileCorrelationChanged(0);
    emit reloadRequest();
}

void ProfileCorrelationItemView::slotDuplicate() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit duplicateRequest(selected.first());
}
