/*
 * File:   LithologicalUnitItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _LITHOLOGICALUNITITEMMODEL_H
#define	_LITHOLOGICALUNITITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class LithologicalUnit;
class LithologicalUnitItem;

class LithologicalUnitItemModel : public StandardItemModel {
    Q_OBJECT
public:
    LithologicalUnitItemModel(QObject* parent = 0);
    virtual ~LithologicalUnitItemModel();
    QModelIndex findIndexForLithologicalUnit(LithologicalUnit* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    LithologicalUnitItem* findItemForLithologicalUnit(int id);

private:
    LithologicalUnitItem* appendItem(LithologicalUnit* oc);

    Project* _project;
};

#endif	/* _LITHOLOGICALUNITITEMMODEL_H */
