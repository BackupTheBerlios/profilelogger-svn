/*
 * File:   BoundaryTypeItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _BOUNDARYTYPEITEMMODEL_H
#define	_BOUNDARYTYPEITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class BoundaryType;
class BoundaryTypeItem;

class BoundaryTypeItemModel : public StandardItemModel {
    Q_OBJECT
public:
    BoundaryTypeItemModel(QObject* parent = 0);
    virtual ~BoundaryTypeItemModel();
    QModelIndex findIndexForBoundaryType(BoundaryType* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    BoundaryTypeItem* findItemForBoundaryType(int id);

private:
    BoundaryTypeItem* appendItem(BoundaryType* oc);

    Project* _project;
};

#endif	/* _BOUNDARYTYPEITEMMODEL_H */
