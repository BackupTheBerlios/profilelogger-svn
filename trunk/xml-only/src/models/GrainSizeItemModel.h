/*
 * File:   GrainSizeItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _GRAINSIZEITEMMODEL_H
#define	_GRAINSIZEITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class GrainSize;
class GrainSizeItem;

class GrainSizeItemModel : public StandardItemModel {
    Q_OBJECT
public:
    GrainSizeItemModel(QObject* parent = 0);
    virtual ~GrainSizeItemModel();
    QModelIndex findIndexForGrainSize(GrainSize* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void slotCurrentProjectChanged(Project* p);
    
protected:
    GrainSizeItem* findItemForGrainSize(int id);

private:
    GrainSizeItem* appendItem(GrainSize* oc);

    Project* _project;
};

#endif	/* _GRAINSIZEITEMMODEL_H */
