/* 
 * File:   BedItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:39
 */

#ifndef _BEDITEMMODEL_H
#define	_BEDITEMMODEL_H

#include "StandardItemModel.h"

class Profile;
class Bed;
class BedItem;

class BedItemModel : public StandardItemModel {
    Q_OBJECT
public:
    BedItemModel(QObject* p = 0);
    virtual ~BedItemModel();

    Bed* getCurrentBed() {
        return _currentBed;
    }

    bool hasCurrentBed() {
        return 0 != _currentBed;
    }

    QModelIndex findIndexForBed(Bed* b);
    
signals:
    void selectRequest(const QModelIndex& idx);
    void currentBedChanged(Bed* b);

public slots:
    void slotCurrentProfileChanged(Profile* p);
    void reload();
    void slotCreateBedOnTop();
    void slotCreateBedAbove(const QModelIndex& idxBedBelow);
    void slotCreateBedBelow(const QModelIndex& idxBedAbove);
    void slotEdit(const QModelIndex& idx);
    void slotMoveUp(const QModelIndex& idx);
    void slotMoveDown(const QModelIndex& idx);
    void slotDelete(QModelIndexList lst);
    void slotDuplicateAndInsertOnTop(const QModelIndex& idx);
    void slotSplitProfileAt(const QModelIndex& idx);
    void slotInsertProfileAbove(Profile* p, const QModelIndex& idx);
    void slotInsertProfileBelow(Profile* p, const QModelIndex& idx);
    void slotDeleteBedsAbove(const QModelIndex& idx);
    void slotDeleteBedsBelow(const QModelIndex& idx);

    void setCurrentBed(Bed* b);

    void slotCreateBedAboveCurrentBed();
    void slotCreateBedBelowCurrentBed();
    void slotEditCurrentBed();
    void slotMoveCurrentBedUp();
    void slotMoveCurrentBedDown();
    void slotDuplicateCurrentBedAndInsertOnTop();
    void slotSplitProfileAtCurrentBed();
    void slotInsertProfileAboveCurrentBed();
    void slotInsertProfileBelowCurrentBed();
    void slotDeleteCurrentBed();
    void slotDeleteBedsAboveCurrentBed();
    void slotDeleteBedsBelowCurrentBed();


private:
    BedItem* appendItem(Bed* b);
    BedItem* findItemForBed(Bed* b);

    Profile* _profile;
    Bed* _currentBed;
};

#endif	/* _BEDITEMMODEL_H */

