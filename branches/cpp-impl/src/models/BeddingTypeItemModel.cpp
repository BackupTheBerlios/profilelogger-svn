/*
 * File:   BeddingTypeItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "BeddingTypeItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "BeddingTypeItem.h"
#include "Project.h"
#include "BeddingTypeEditorDialog.h"
#include "BeddingType.h"

class Project;

BeddingTypeItemModel::BeddingTypeItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

BeddingTypeItemModel::~BeddingTypeItemModel() {
}

void BeddingTypeItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void BeddingTypeItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Bedding Type");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }

    QList<BeddingType*>::iterator it = _project->getFirstBeddingType();
    QList<BeddingType*>::iterator last = _project->getLastBeddingType();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void BeddingTypeItemModel::createNew() {
    BeddingType* p = _project->createBeddingType();
    BeddingTypeEditorDialog* dlg = new BeddingTypeEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

BeddingTypeItem* BeddingTypeItemModel::appendItem(BeddingType* p) {
    BeddingTypeItem* i = new BeddingTypeItem(p);
    appendRow(i);
    return i;
}

void BeddingTypeItemModel::slotEditRequested(const QModelIndex& idx) {
    BeddingTypeItem* itm = (BeddingTypeItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    BeddingTypeEditorDialog* dlg = new BeddingTypeEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getBeddingType());
    dlg->exec();
    int id = dlg->getBeddingType()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForBeddingType(id)));
}

BeddingTypeItem* BeddingTypeItemModel::findItemForBeddingType(int id) {
    for (int r = 0; r < rowCount(); r++) {
        BeddingTypeItem* ret = (BeddingTypeItem*) item(r);
        if (ret->getBeddingType()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void BeddingTypeItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        BeddingTypeItem* itm = (BeddingTypeItem*) itemFromIndex(*it);
        _project->deleteBeddingType(itm->getBeddingType());
    }
    reload();
}

QModelIndex BeddingTypeItemModel::findIndexForBeddingType(BeddingType* q) {
    if (!q) {
        return QModelIndex();
    }

    BeddingTypeItem* itm = findItemForBeddingType(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
