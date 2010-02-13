/*
 * File:   BeddingTypeItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _BEDDINGTYPEITEMMODEL_H
#define	_BEDDINGTYPEITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class BeddingType;
class BeddingTypeItem;

class BeddingTypeItemModel : public StandardItemModel {
    Q_OBJECT
public:
    BeddingTypeItemModel(QObject* parent = 0);
    virtual ~BeddingTypeItemModel();
    QModelIndex findIndexForBeddingType(BeddingType* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    BeddingTypeItem* findItemForBeddingType(int id);

private:
    BeddingTypeItem* appendItem(BeddingType* oc);

    Project* _project;
};

#endif	/* _BEDDINGTYPEITEMMODEL_H */
