/* 
 * File:   BedItemView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:40
 */

#ifndef _BEDITEMVIEW_H
#define	_BEDITEMVIEW_H

#include "TreeView.h"

class Profile;
class Bed;
class BedItemModel;

class BedItemView : public TreeView {
    Q_OBJECT
public:
    BedItemView(QWidget* p, BedItemModel* model);
    virtual ~BedItemView();

signals:
    void selectItemRequest(const QModelIndex& idx);
    void currentBedChanged(Bed* bed);
    void reloadRequest();
    void createBedOnTopRequest();
    void createBedAboveRequest(const QModelIndex& bedIndexBelow);
    void createBedBelowRequest(const QModelIndex& bedIndexBelow);
    void editRequest(const QModelIndex& idx);
    void moveUpRequest(const QModelIndex& idx);
    void moveDownRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void duplicateAndInsertOnTopRequest(const QModelIndex& idx);
    void splitProfileAtRequest(const QModelIndex& idx);
    void deleteBedsAboveRequest(const QModelIndex& idx);
    void deleteBedsBelowRequest(const QModelIndex& idx);

public slots:
    void selectBed(Bed* b);
    void slotCurrentProfileChanged(Profile* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotIndexActivated(const QModelIndex&);
    void slotSelectItemRequested(const QModelIndex& idx);

    void slotReload();
    void slotCreateNewOnTop();
    void slotCreateAboveCurrent();
    void slotCreateBelowCurrent();
    void slotMoveUp();
    void slotMoveDown();
    void slotEdit();
    void slotDelete();
    void slotReloaded();
    void slotDuplicateAndInsertOnTop();
    void slotSplitProfileHere();
    void slotDeleteBedsAboveCurrentBed();
    void slotDeleteBedsBelowCurrentBed();
    
private:
    Profile* _profile;
};

#endif	/* _BEDITEMVIEW_H */

