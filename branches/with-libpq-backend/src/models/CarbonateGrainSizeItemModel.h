/*
 * File:   CarbonateGrainSizeItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _CARBONATEGRAINSIZEITEMMODEL_H
#define	_CARBONATEGRAINSIZEITEMMODEL_H

#include "GrainSizeItemModel.h"
#include "GrainSizeView.h"

class Project;
class CarbonateGrainSize;
class CarbonateGrainSizeItem;

class CarbonateGrainSizeItemModel : public GrainSizeItemModel {
    Q_OBJECT
public:
    CarbonateGrainSizeItemModel(QObject* parent = 0);
    virtual ~CarbonateGrainSizeItemModel();
    QModelIndex findIndexForCarbonateGrainSize(CarbonateGrainSize* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void slotCurrentProjectChanged(Project* p);

protected:
    CarbonateGrainSizeItem* findItemForCarbonateGrainSize(int id);

private:
    CarbonateGrainSizeItem* appendItem(CarbonateGrainSize* oc);

    Project* _project;
};

#endif	/* _CARBONATEGRAINSIZEITEMMODEL_H */
