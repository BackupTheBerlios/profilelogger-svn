/*
 * File:   LithologicalUnitTypeItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _LITHOLOGICALUNITTYPEITEMMODEL_H
#define	_LITHOLOGICALUNITTYPEITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class LithologicalUnitType;
class LithologicalUnitTypeItem;

class LithologicalUnitTypeItemModel : public StandardItemModel {
    Q_OBJECT
public:
    LithologicalUnitTypeItemModel(QObject* parent = 0);
    virtual ~LithologicalUnitTypeItemModel();
    QModelIndex findIndexForLithologicalUnitType(LithologicalUnitType* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    LithologicalUnitTypeItem* findItemForLithologicalUnitType(int id);

private:
    LithologicalUnitTypeItem* appendItem(LithologicalUnitType* oc);

    Project* _project;
};

#endif	/* _LITHOLOGICALUNITTYPEITEMMODEL_H */
