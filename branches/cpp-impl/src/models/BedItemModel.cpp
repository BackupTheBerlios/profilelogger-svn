/* 
 * File:   BedItemModel.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 11:39
 */

#include "BedItemModel.h"

#include <QMessageBox>
#include <QApplication>

#include "MainWindow.h"
#include "StandardItemModel.h"
#include "ProfileLogger.h"
#include "Profile.h"
#include "BedItem.h"
#include "BedEditorDialog.h"
#include "Bed.h"
#include "WorkWidget.h"
#include "ProfileSelectorDialog.h"

BedItemModel::BedItemModel(QObject* p)
: StandardItemModel(p),
_profile(0),
_currentBed(0) {
    setSortRole(Qt::UserRole);
}

BedItemModel::~BedItemModel() {
}

void BedItemModel::slotCurrentProfileChanged(Profile* p) {
    _profile = p;

    reload();
}

void BedItemModel::reload() {
    _currentBed = 0;
    clear();

    QStringList hh;
    hh << tr("Beds");
    setHorizontalHeaderLabels(hh);

    if (!_profile) {
        return;
    }

    int bedCnt = _profile->getBedCount();

    for (int pos = 0; pos < bedCnt; pos++) {
        appendItem(_profile->getBedByPosition(pos));
    }

    emit reloaded();
    reset();
}

BedItem* BedItemModel::appendItem(Bed* b) {
    BedItem* itm = new BedItem(b);
    appendRow(itm);
    return itm;
}

void BedItemModel::slotCreateBedOnTop() {
    Bed* bed = _profile->createBed();

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Create Bed On Top?"),
            tr("Create Bed On Top Of Profile?"),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    BedEditorDialog* dlg = new BedEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), bed);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForBed(bed)));
}

void BedItemModel::slotCreateBedAbove(const QModelIndex& idxBedBelow) {
    if (!idxBedBelow.isValid()) {
        return;
    }

    BedItem* bitm = (BedItem*) itemFromIndex(idxBedBelow);

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Create Bed Above?"),
            tr("Create Bed Above Bed %1?").arg(bitm->getBed()->getPosition()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    Bed* bed = _profile->createBed(0, bitm->getBed()->getPosition());

    BedEditorDialog* dlg = new BedEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), bed);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForBed(bed)));
}

void BedItemModel::slotCreateBedBelow(const QModelIndex& idxBedAbove) {
    if (!idxBedAbove.isValid()) {
        return;
    }

    BedItem* bitm = (BedItem*) itemFromIndex(idxBedAbove);

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Create Bed Below?"),
            tr("Create Bed Below Bed %1?").arg(bitm->getBed()->getPosition()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    Bed* bed = _profile->createBed(0, bitm->getBed()->getPosition() - 1);

    BedEditorDialog* dlg = new BedEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), bed);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForBed(bed)));
}

void BedItemModel::slotEdit(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    BedItem* itm = (BedItem*) itemFromIndex(idx);
    Bed* bed = itm->getBed();

    BedEditorDialog* dlg = new BedEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), bed);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForBed(bed)));
}

BedItem* BedItemModel::findItemForBed(Bed* b) {
    if (!b) {
        return 0;
    }

    int max = rowCount();
    for (int r = 0; r < max; r++) {
        BedItem* itm = (BedItem*) item(r);
        if (itm->getBed()->getId() == b->getId()) {
            return itm;
        }
    }
    return 0;
}

void BedItemModel::slotMoveDown(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    BedItem* itm = ((BedItem*) itemFromIndex(idx));

    if (!itm) {
        return;
    }

    Bed* bed = itm->getBed();

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Move Bed Down?"),
            tr("Move Bed %1 down?").arg(bed->getPosition()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    _profile->moveBedDown(bed);
    reload();
}

void BedItemModel::slotMoveUp(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    BedItem* itm = ((BedItem*) itemFromIndex(idx));

    if (!itm) {
        return;
    }

    Bed* bed = itm->getBed();

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Move Bed Up?"),
            tr("Move Bed %1 Up?").arg(bed->getPosition()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    _profile->moveBedUp(bed);
    reload();
}

void BedItemModel::slotDelete(QModelIndexList lst) {
    if (lst.size() < 1) {
        return;
    }

    QStringList names;
    QList<Bed*> beds;

    for (QModelIndexList::iterator it = lst.begin(); it != lst.end(); it++) {
        BedItem* itm = (BedItem*) itemFromIndex(*it);
        names << QString::number(itm->getBed()->getPosition());

        beds << itm->getBed();
    }

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Delete beds?"),
            tr("Delete beds %1?").arg(names.join(", ")),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    for (QList<Bed*>::iterator it = beds.begin(); it != beds.end(); it++) {
        _profile->deleteBed(*it);
    }

    reload();
}

void BedItemModel::slotDeleteBedsAbove(const QModelIndex& idx) {
    BedItem* itm = (BedItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    Bed* bed = itm->getBed();

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Delete beds above %1?").arg(bed->getPosition()),
            tr("Delete beds above bed %1?").arg(bed->getPosition()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    _profile->deleteBedsAbove(bed);

    reload();
}

void BedItemModel::slotDeleteBedsBelow(const QModelIndex& idx) {
    BedItem* itm = (BedItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    Bed* bed = itm->getBed();

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Delete beds below %1?").arg(bed->getPosition()),
            tr("Delete beds below bed %1?").arg(bed->getPosition()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    _profile->deleteBedsBelow(bed);

    reload();
}

void BedItemModel::slotSplitProfileAt(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    BedItem* itm = (BedItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    Bed* bed = itm->getBed();

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Split Profile?"),
            tr("Split Profile at bed %1?").arg(bed->getPosition()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    _profile->deleteBedsAbove(bed);
    itm->getBed()->getProfile()->splitAtBed(itm->getBed());

    reload();
}

void BedItemModel::slotDuplicateAndInsertOnTop(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    BedItem* itm = (BedItem*) itemFromIndex(idx);
    if (!itm) {
        return;
    }

    Bed* src = itm->getBed();
    if (!src) {
        return;
    }

    if (QMessageBox::Yes != QMessageBox::question((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Duplicate Bed and insert at top?"),
            tr("Duplicate bed %1 and insert at top?").arg(src->getPosition()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    Bed* bed = _profile->copyBed(src);
    /*
    Bed* bed = _profile->createBed();
    bed->getHeight()->setValue(src->getHeight()->getValue());
    bed->getHeight()->setUnit(src->getHeight()->getUnit());
    bed->setName(src->getName());
    bed->setLithology(src->getLithology());
    bed->setBaseCarbonateGrainSize(src->getBaseCarbonateGrainSize());
    bed->setBaseClasticGrainSize(src->getBaseClasticGrainSize());
    bed->setBeddingType(src->getBeddingType());
    bed->setColor(src->getColor());
    bed->setDescription(src->getDescription());
    bed->setFacies(src->getFacies());
    bed->setGrainSizeMode(src->getGrainSizeMode());
    bed->setOutcropQuality(src->getOutcropQuality());
    bed->setTopBoundaryType(src->getTopBoundaryType());
    bed->setTopCarbonateGrainSize(src->getTopCarbonateGrainSize());
    bed->setTopClasticGrainSize(src->getTopClasticGrainSize());

    for (QList<Fossil*>::iterator it = src->getFirstFossil();
            it != src->getLastFossil();
            it++) {
        bed->addFossil(*it);
    }

    for (QList<SedimentStructure*>::iterator it = src->getFirstSedimentStructure();
            it != src->getLastSedimentStructure();
            it++) {
        bed->addSedimentStructure(*it);
    }

    for (QList<CustomSymbol*>::iterator it = src->getFirstCustomSymbol();
            it != src->getLastCustomSymbol();
            it++) {
        bed->addCustomSymbol(*it);
    }
     */
    BedEditorDialog* dlg = new BedEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), bed);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForBed(bed)));
}

void BedItemModel::setCurrentBed(Bed* b) {
    if (b != _currentBed) {
        emit currentBedChanged(b);
    }

    _currentBed = b;
}

void BedItemModel::slotCreateBedAboveCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }

    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }

    slotCreateBedAbove(idx);
}

void BedItemModel::slotCreateBedBelowCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }

    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }

    slotCreateBedBelow(idx);
}

void BedItemModel::slotEditCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }

    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }

    slotEdit(idx);
}

void BedItemModel::slotMoveCurrentBedUp() {
    if (!hasCurrentBed()) {
        return;
    }
    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }

    slotMoveUp(idx);
}

void BedItemModel::slotMoveCurrentBedDown() {
    if (!hasCurrentBed()) {
        return;
    }
    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }

    slotMoveDown(idx);
}

void BedItemModel::slotDuplicateCurrentBedAndInsertOnTop() {
    if (!hasCurrentBed()) {
        return;
    }
    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }

    slotDuplicateAndInsertOnTop(idx);
}

void BedItemModel::slotSplitProfileAtCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }
    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }

    slotSplitProfileAt(idx);
}

void BedItemModel::slotDeleteCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }
    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }

    QModelIndexList lst;
    lst << idx;
    slotDelete(lst);
}

void BedItemModel::slotDeleteBedsAboveCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }
    QModelIndex idx = findIndexForBed(getCurrentBed());
    if (!idx.isValid()) {
        return;
    }
    slotDeleteBedsAbove(idx);
}

void BedItemModel::slotDeleteBedsBelowCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }

    QModelIndex idx = findIndexForBed(getCurrentBed());

    if (!idx.isValid()) {
        return;
    }

    slotDeleteBedsBelow(idx);
}

QModelIndex BedItemModel::findIndexForBed(Bed* b) {
    BedItem* itm = findItemForBed(b);

    if (!itm) {
        return QModelIndex();
    }

    return indexFromItem(itm);
}

void BedItemModel::slotInsertProfileAboveCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }

    QModelIndex idx = findIndexForBed(getCurrentBed());

    if (!idx.isValid()) {
        return;
    }

    ProfileSelectorDialog* dlg = new ProfileSelectorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow());

    if (QDialog::Accepted != dlg->exec()) {
        return;
    }

    Profile *otherP = dlg->getSelectedProfile();

    if (!otherP) {
        return;
    }

    slotInsertProfileAbove(otherP, idx);
}

void BedItemModel::slotInsertProfileBelowCurrentBed() {
    if (!hasCurrentBed()) {
        return;
    }

    QModelIndex idx = findIndexForBed(getCurrentBed());

    if (!idx.isValid()) {
        return;
    }

    ProfileSelectorDialog* dlg = new ProfileSelectorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow());

    if (QDialog::Accepted != dlg->exec()) {
        return;
    }

    Profile *otherP = dlg->getSelectedProfile();

    if (!otherP) {
        return;
    }

    slotInsertProfileBelow(otherP, idx);
}

void BedItemModel::slotInsertProfileAbove(Profile* p, const QModelIndex& idx) {
    BedItem* itm = (BedItem*) itemFromIndex(idx);
    
    if (!itm) {
        return;
    }

    int lastPos = itm->getBed()->getPosition();
    
    for (QList<Bed*>::iterator it = p->getFirstBed(); it != p->getLastBed(); it++) {
        (void) _profile->copyBed(*it, 0, lastPos);
        lastPos++;
    }

    reload();
}

void BedItemModel::slotInsertProfileBelow(Profile* p, const QModelIndex& idx) {
    //FIXME: this is seriously buggy and currently not available in the gui
    BedItem* itm = (BedItem*) itemFromIndex(idx);

    if (!itm) {
        return;
    }

    int lastPos = itm->getBed()->getPosition() - 1;

    QList<Bed*>::iterator it = p->getLastBed();
    QList<Bed*> beds;
    
    for (QList<Bed*>::iterator it = p->getLastBed(); it != p->getFirstBed(); it--) {
        beds.prepend(*it);
        
    }

    for(int i = 0; i < beds.size(); i++) {
        Bed* b = beds.at(i);
        lastPos += i;
        (void) _profile->copyBed(b, 0, lastPos);
    }

    reload();
}
