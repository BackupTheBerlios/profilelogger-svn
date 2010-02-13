/*
 * File:   FossilInBedItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _FOSSILINBEDITEMMODEL_H
#define	_FOSSILINBEDITEMMODEL_H

#include "StandardItemModel.h"

class Bed;
class Fossil;
class FossilItem;

class FossilInBedItemModel : public StandardItemModel {
    Q_OBJECT
public:
    FossilInBedItemModel(QObject* parent = 0);
    virtual ~FossilInBedItemModel();
    QModelIndex findIndexForFossil(Fossil* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void slotCurrentBedChanged(Bed* b);
    void slotDeleteRequested(QModelIndexList list);

protected:
    FossilItem* findItemForFossil(int id);
    
private:
    FossilItem* appendItem(Fossil* oc);

    Bed* _bed;
};

#endif	/* _FOSSILINBEDITEMMODEL_H */
