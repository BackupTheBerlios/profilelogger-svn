/*
 * File:   BedCorrelationItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:39
 */

#include <QMap>
#include <QFileDialog>
#include <QMessageBox>
#include <QFile>
#include <QTextStream>
#include <QDir>
#include <QFileInfo>

#include "BedCorrelationItemModel.h"

#include "StandardItemModel.h"
#include "ProfileLogger.h"
#include "ProfileCorrelation.h"
#include "Project.h"
#include "BedCorrelationItem.h"
#include "BedCorrelationEditorDialog.h"
#include "BedCorrelation.h"
#include "WorkWidget.h"
#include "MainWindow.h"

BedCorrelationItemModel::BedCorrelationItemModel(QObject* p)
: StandardItemModel(p),
_profileCorrelation(0) {
    setSortRole(Qt::UserRole);
}

BedCorrelationItemModel::~BedCorrelationItemModel() {
}

void BedCorrelationItemModel::slotCurrentProfileCorrelationChanged(ProfileCorrelation* p) {
    _profileCorrelation = p;

    reload();
}

void BedCorrelationItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Bed Correlations");
    setHorizontalHeaderLabels(hh);

    if (!_profileCorrelation) {
        return;
    }

    for (QList<BedCorrelation*>::iterator it = _profileCorrelation->getFirstBedCorrelation();
            it != _profileCorrelation->getLastBedCorrelation();
            it++) {
        appendItem(*it);
    }

    emit reloaded();
}

BedCorrelationItem* BedCorrelationItemModel::appendItem(BedCorrelation* b) {
    BedCorrelationItem* itm = new BedCorrelationItem(b);
    appendRow(itm);
    return itm;
}

void BedCorrelationItemModel::slotCreate() {
    BedCorrelation* bedCorrelation = _profileCorrelation->createBedCorrelation();

    BedCorrelationEditorDialog* dlg = new BedCorrelationEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            bedCorrelation);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForBedCorrelation(bedCorrelation)));
}

void BedCorrelationItemModel::slotEdit(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    BedCorrelationItem* itm = (BedCorrelationItem*) itemFromIndex(idx);
    BedCorrelation* bedCorrelation = itm->getBedCorrelation();

    BedCorrelationEditorDialog* dlg = new BedCorrelationEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            bedCorrelation);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForBedCorrelation(bedCorrelation)));
}

BedCorrelationItem* BedCorrelationItemModel::findItemForBedCorrelation(BedCorrelation* b) {
    if (!b) {
        return 0;
    }

    int max = rowCount();
    for (int r = 0; r < max; r++) {
        BedCorrelationItem* itm = (BedCorrelationItem*) item(r);
        if (itm->getBedCorrelation()->getId() == b->getId()) {
            return itm;
        }
    }
    return 0;
}

void BedCorrelationItemModel::slotDelete(QModelIndexList lst) {
    for (QModelIndexList::iterator it = lst.begin(); it != lst.end(); it++) {
        BedCorrelationItem* itm = (BedCorrelationItem*) itemFromIndex(*it);
        _profileCorrelation->deleteBedCorrelation(itm->getBedCorrelation());
    }
    reload();
}

