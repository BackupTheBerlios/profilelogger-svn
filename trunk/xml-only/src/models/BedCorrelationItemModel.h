/*
 * File:   BedCorrelationItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:39
 */

#ifndef _BEDCORRELATIONITEMMODEL_H
#define	_BEDCORRELATIONITEMMODEL_H

#include "StandardItemModel.h"

class ProfileCorrelation;
class BedCorrelation;
class BedCorrelationItem;

class BedCorrelationItemModel : public StandardItemModel {
    Q_OBJECT
public:
    BedCorrelationItemModel(QObject* p = 0);
    virtual ~BedCorrelationItemModel();

signals:
    void selectRequest(const QModelIndex& idx);

public slots:
    void slotCurrentProfileCorrelationChanged(ProfileCorrelation* p);
    void reload();

    void slotCreate();
    void slotEdit(const QModelIndex& idx);
    void slotDelete(QModelIndexList lst);
    
private:
    BedCorrelationItem* appendItem(BedCorrelation* b);
    BedCorrelationItem* findItemForBedCorrelation(BedCorrelation* b);

    ProfileCorrelation* _profileCorrelation;
};

#endif	/* _BEDCORRELATIONITEMMODEL_H */

