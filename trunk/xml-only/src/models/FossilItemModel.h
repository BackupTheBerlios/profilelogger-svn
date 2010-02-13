/*
 * File:   FossilItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _FOSSILITEMMODEL_H
#define	_FOSSILITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class Fossil;
class FossilItem;

class FossilItemModel : public StandardItemModel {
    Q_OBJECT
public:
    FossilItemModel(QObject* parent = 0);
    virtual ~FossilItemModel();
    QModelIndex findIndexForFossil(Fossil* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    FossilItem* findItemForFossil(int id);

private:
    FossilItem* appendItem(Fossil* oc);

    Project* _project;
};

#endif	/* _FOSSILITEMMODEL_H */
