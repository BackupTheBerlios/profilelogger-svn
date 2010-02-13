/*
 * File:   CustomSymbolItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "CustomSymbolItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "CustomSymbolItem.h"
#include "Project.h"
#include "CustomSymbolEditorDialog.h"
#include "CustomSymbol.h"

class Project;

CustomSymbolItemModel::CustomSymbolItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect(static_cast<ProfileLogger*> (QApplication::instance()),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

CustomSymbolItemModel::~CustomSymbolItemModel() {
}

void CustomSymbolItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void CustomSymbolItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Custom Symbol");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }
    
    QList<CustomSymbol*>::iterator it = _project->getFirstCustomSymbol();
    QList<CustomSymbol*>::iterator last = _project->getLastCustomSymbol();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void CustomSymbolItemModel::createNew() {
    CustomSymbol* p = _project->createCustomSymbol();
    CustomSymbolEditorDialog* dlg = new CustomSymbolEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

CustomSymbolItem* CustomSymbolItemModel::appendItem(CustomSymbol* p) {
    CustomSymbolItem* i = new CustomSymbolItem(p);
    appendRow(i);
    return i;
}

void CustomSymbolItemModel::slotEditRequested(const QModelIndex& idx) {
    CustomSymbolItem* itm = (CustomSymbolItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    CustomSymbolEditorDialog* dlg = new CustomSymbolEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getCustomSymbol());
    dlg->exec();
    int id = dlg->getCustomSymbol()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForCustomSymbol(id)));
}

CustomSymbolItem* CustomSymbolItemModel::findItemForCustomSymbol(int id) {
    for (int r = 0; r < rowCount(); r++) {
        CustomSymbolItem* ret = (CustomSymbolItem*) item(r);
        if (ret->getCustomSymbol()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void CustomSymbolItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        CustomSymbolItem* itm = (CustomSymbolItem*) itemFromIndex(*it);
        _project->deleteCustomSymbol(itm->getCustomSymbol());
    }
    reload();
}

QModelIndex CustomSymbolItemModel::findIndexForCustomSymbol(CustomSymbol* q) {
    if (!q) {
        return QModelIndex();
    }

    CustomSymbolItem* itm = findItemForCustomSymbol(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
