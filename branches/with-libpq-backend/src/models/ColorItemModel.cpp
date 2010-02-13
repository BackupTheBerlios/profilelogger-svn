/*
 * File:   ColorItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "ColorItemModel.h"

#include "ProfileLogger.h"
#include "MainWindow.h"
#include "ProfileLogger.h"
#include "ColorItem.h"
#include "Project.h"
#include "ColorEditorDialog.h"
#include "Color.h"

class Project;

ColorItemModel::ColorItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

ColorItemModel::~ColorItemModel() {
}

void ColorItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void ColorItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Color");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }
    
    QList<Color*>::iterator it = _project->getFirstColor();
    QList<Color*>::iterator last = _project->getLastColor();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void ColorItemModel::createNew() {
    Color* p = _project->createColor();
    ColorEditorDialog* dlg = new ColorEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

ColorItem* ColorItemModel::appendItem(Color* p) {
    ColorItem* i = new ColorItem(p);
    appendRow(i);
    return i;
}

void ColorItemModel::slotEditRequested(const QModelIndex& idx) {
    ColorItem* itm = (ColorItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    ColorEditorDialog* dlg = new ColorEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getColor());
    dlg->exec();
    int id = dlg->getColor()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForColor(id)));
}

ColorItem* ColorItemModel::findItemForColor(int id) {
    for (int r = 0; r < rowCount(); r++) {
        ColorItem* ret = (ColorItem*) item(r);
        if (ret->getColor()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void ColorItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        ColorItem* itm = (ColorItem*) itemFromIndex(*it);
        _project->deleteColor(itm->getColor());
    }
    reload();
}

QModelIndex ColorItemModel::findIndexForColor(Color* q) {
    if (!q) {
        return QModelIndex();
    }

    ColorItem* itm = findItemForColor(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
