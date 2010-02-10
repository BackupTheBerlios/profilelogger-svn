/*
 * File:   ClasticGrainSizeItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _CLASTICGRAINSIZEITEMMODEL_H
#define	_CLASTICGRAINSIZEITEMMODEL_H

#include "GrainSizeItemModel.h"
#include "GrainSizeView.h"

class Project;
class ClasticGrainSize;
class ClasticGrainSizeItem;

class ClasticGrainSizeItemModel : public GrainSizeItemModel {
    Q_OBJECT
public:
    ClasticGrainSizeItemModel(QObject* parent = 0);
    virtual ~ClasticGrainSizeItemModel();
    QModelIndex findIndexForClasticGrainSize(ClasticGrainSize* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void slotCurrentProjectChanged(Project* p);

protected:
    ClasticGrainSizeItem* findItemForClasticGrainSize(int id);

private:
    ClasticGrainSizeItem* appendItem(ClasticGrainSize* oc);

    Project* _project;
};

#endif	/* _CLASTICGRAINSIZEITEMMODEL_H */
