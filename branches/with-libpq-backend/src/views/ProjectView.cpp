#include "ProjectView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "ProjectItemModel.h"
#include "ProjectItem.h"
#include "ProfileLogger.h"
#include "Project.h"

ProjectView::ProjectView(QWidget* p, ProjectItemModel* model)
: TreeView(p) {
    setModel(model);
    connect(model, SIGNAL(reloaded()), this, SLOT(slotReloaded()));

    setContextMenuPolicy(Qt::CustomContextMenu);

    connect(this, SIGNAL(customContextMenuRequested(const QPoint&)), this, SLOT(slotCustomContextMenuRequested(const QPoint&)));
    //    connect(static_cast<ProfileLogger*> (QApplication::instance()), SIGNAL(currentProjectChanged(Project*)), this, SLOT(slotCurrentProjectChanged(Project*)));
    connect(this, SIGNAL(activated(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(clicked(const QModelIndex&)), this, SLOT(slotIndexActivated(const QModelIndex&)));
    connect(this, SIGNAL(reloadRequest()), model, SLOT(reload()));

    connect(model, SIGNAL(selectItemRequest(const QModelIndex&)), this, SLOT(slotSelectItemRequested(const QModelIndex&)));
    connect(this, SIGNAL(editRequest(const QModelIndex&)), model, SLOT(slotEditRequested(const QModelIndex&)));
    connect(this, SIGNAL(deleteRequest(QModelIndexList)), model, SLOT(slotDeleteRequested(QModelIndexList)));
}

ProjectView::~ProjectView() {
}

/*void ProjectView::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
    }*/

void ProjectView::slotCustomContextMenuRequested(const QPoint& p) {
    QMenu* m = new QMenu(this);

    QAction* reloadA = new QAction(tr("Reload"), this);
    QAction* createA = new QAction(tr("Create..."), this);
    QAction* editA = new QAction(tr("Edit..."), this);
    QAction* deleteA = new QAction(tr("Delete"), this);

    connect(reloadA, SIGNAL(activated()), this, SLOT(slotReload()));
    connect(createA, SIGNAL(activated()), (ProjectItemModel*) model(), SLOT(createNew()));
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

void ProjectView::slotSelectItemRequested(const QModelIndex& idx) {
    if (!selectionModel()) {
        setSelectionModel(new QItemSelectionModel(model()));
    }

    selectionModel()->select(idx, QItemSelectionModel::ClearAndSelect);
    selectionModel()->setCurrentIndex(idx, QItemSelectionModel::ClearAndSelect);

    scrollTo(idx, QAbstractItemView::EnsureVisible);
}

void ProjectView::slotEdit() {
    QModelIndexList selected = selectedIndexes();

    if (selected.size() != 1) {
        return;
    }

    emit editRequest(selected.first());
}

void ProjectView::slotDelete() {
    QModelIndexList selected = selectedIndexes();

    QStringList names;
    for (QModelIndexList::iterator it = selected.begin();
            it != selected.end();
            it++) {
        ProjectItem* itm = (ProjectItem*) ((ProjectItemModel*) model())->itemFromIndex(*it);
        if (itm) {
            names << itm->getProject()->getName();
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

void ProjectView::slotIndexActivated(const QModelIndex& idx) {
  (void) idx;
  /*
    if (!idx.isValid()) {
      emit currentProjectChanged(0);
        return;
    }

    ProjectItem* itm = (ProjectItem*) (((ProjectItemModel*) model())->itemFromIndex(idx));

     if (!itm) {
        emit currentProjectChanged(0);
    } else {
        emit currentProjectChanged(itm->getProject());
	}*/
}

void ProjectView::slotReload() {
  //emit currentProjectChanged(0);
    emit reloadRequest();
}

void ProjectView::selectProject(Project* q) {
    selectionModel()->clear();
    if (!q) {
        return;
    }

    QModelIndex idx = ((ProjectItemModel*)model())->findIndexForProject(q);
    if (!idx.isValid()) {
        return;
    }
    slotSelectItemRequested(idx);
}
