/*
 * File:   SedimentStructureItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _SEDIMENTSTRUCTUREITEMMODEL_H
#define	_SEDIMENTSTRUCTUREITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class SedimentStructure;
class SedimentStructureItem;

class SedimentStructureItemModel : public StandardItemModel {
    Q_OBJECT
public:
    SedimentStructureItemModel(QObject* parent = 0);
    virtual ~SedimentStructureItemModel();
    QModelIndex findIndexForSedimentStructure(SedimentStructure* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    SedimentStructureItem* findItemForSedimentStructure(int id);

private:
    SedimentStructureItem* appendItem(SedimentStructure* oc);

    Project* _project;
};

#endif	/* _SEDIMENTSTRUCTUREITEMMODEL_H */
