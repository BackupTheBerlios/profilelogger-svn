/* 
 * File:   OutcropQualityItemModel.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 16:42
 */

#include "OutcropQualityItemModel.h"

#include <QApplication>

#include "MainWindow.h"
#include "ProfileLogger.h"
#include "OutcropQualityItem.h"
#include "Project.h"
#include "OutcropQualityEditorDialog.h"
#include "OutcropQuality.h"

class Project;

OutcropQualityItemModel::OutcropQualityItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
    connect((static_cast<ProfileLogger*> (QApplication::instance())),
            SIGNAL(currentProjectChanged(Project*)),
            this,
            SLOT(slotCurrentProjectChanged(Project*)));
}

OutcropQualityItemModel::~OutcropQualityItemModel() {
}

void OutcropQualityItemModel::slotCurrentProjectChanged(Project* p) {
    _project = p;
    reload();
}

void OutcropQualityItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Outcrop Quality");
    setHorizontalHeaderLabels(hh);

    if (!_project) {
        return;
    }
    
    QList<OutcropQuality*>::iterator it = _project->getFirstOutcropQuality();
    QList<OutcropQuality*>::iterator last = _project->getLastOutcropQuality();

    while (it != last) {
        appendItem(*it);
        it++;
    }

    emit reloaded();
}

void OutcropQualityItemModel::createNew() {
    OutcropQuality* p = _project->createOutcropQuality();
    OutcropQualityEditorDialog* dlg = new OutcropQualityEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), p);
    dlg->exec();
    emit selectItemRequest(indexFromItem(appendItem(p)));
}

OutcropQualityItem* OutcropQualityItemModel::appendItem(OutcropQuality* p) {
    OutcropQualityItem* i = new OutcropQualityItem(p);
    appendRow(i);
    return i;
}

void OutcropQualityItemModel::slotEditRequested(const QModelIndex& idx) {
    OutcropQualityItem* itm = (OutcropQualityItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    OutcropQualityEditorDialog* dlg = new OutcropQualityEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), itm->getOutcropQuality());
    dlg->exec();
    int id = dlg->getOutcropQuality()->getId();
    reload();
    emit selectItemRequest(indexFromItem(findItemForOutcropQuality(id)));
}

OutcropQualityItem* OutcropQualityItemModel::findItemForOutcropQuality(int id) {
    for (int r = 0; r < rowCount(); r++) {
        OutcropQualityItem* ret = (OutcropQualityItem*) item(r);
        if (ret->getOutcropQuality()->getId() == id) {
            return ret;
        }
    }
    return 0;
}

void OutcropQualityItemModel::slotDeleteRequested(QModelIndexList list) {
    for (QModelIndexList::iterator it = list.begin();
            it != list.end();
            it++) {
        OutcropQualityItem* itm = (OutcropQualityItem*) itemFromIndex(*it);
        _project->deleteOutcropQuality(itm->getOutcropQuality());
    }
    reload();
}

QModelIndex OutcropQualityItemModel::findIndexForOutcropQuality(OutcropQuality* q) {
    if (!q) {
        return QModelIndex();
    }

    OutcropQualityItem* itm = findItemForOutcropQuality(q->getId());
    if (!itm) {
        return QModelIndex();
    }
    return indexFromItem(itm);
}
