/*
 * File:   BedCorrelationItemView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:40
 */

#ifndef _BEDCORRELATIONITEMVIEW_H
#define	_BEDCORRELATIONITEMVIEW_H

#include "TreeView.h"

class ProfileCorrelation;
class BedCorrelation;
class BedCorrelationItemModel;

class BedCorrelationItemView : public TreeView {
    Q_OBJECT
public:
    BedCorrelationItemView(QWidget* p, BedCorrelationItemModel* model);
    virtual ~BedCorrelationItemView();

signals:
    void currentBedCorrelationChanged(BedCorrelation* bed);
    void reloadRequest();
    void createBedCorrelationRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    
public slots:
    void slotCurrentProfileCorrelationChanged(ProfileCorrelation* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotIndexActivated(const QModelIndex&);

    void slotReload();
    void slotCreate();
    void slotEdit();
    void slotDelete();
    void slotReloaded();
    
private:
    ProfileCorrelation* _profileCorrelation;
};

#endif	/* _BEDCORRELATIONITEMVIEW_H */
