/*
 * File:   SedimentStructureInBedItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _SEDIMENTSTRUCTUREINBEDITEMMODEL_H
#define	_SEDIMENTSTRUCTUREINBEDITEMMODEL_H

#include "StandardItemModel.h"

class Bed;
class SedimentStructure;
class SedimentStructureItem;

class SedimentStructureInBedItemModel : public StandardItemModel {
    Q_OBJECT
public:
    SedimentStructureInBedItemModel(QObject* parent = 0);
    virtual ~SedimentStructureInBedItemModel();
    QModelIndex findIndexForSedimentStructure(SedimentStructure* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void slotCurrentBedChanged(Bed* b);
    void slotDeleteRequested(QModelIndexList list);

protected:
    SedimentStructureItem* findItemForSedimentStructure(int id);

private:
    SedimentStructureItem* appendItem(SedimentStructure* oc);

    Bed* _bed;
};

#endif	/* _SEDIMENTSTRUCTUREINBEDITEMMODEL_H */
