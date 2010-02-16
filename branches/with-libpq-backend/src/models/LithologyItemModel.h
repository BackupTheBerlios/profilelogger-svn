/*
 * File:   LithologyItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _LITHOLOGYITEMMODEL_H
#define	_LITHOLOGYITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class Lithology;
class LithologyItem;
class LithologyManager;

class LithologyItemModel : public StandardItemModel {
    Q_OBJECT
public:
    LithologyItemModel(QObject* parent = 0);
    virtual ~LithologyItemModel();
    QModelIndex findIndexForLithology(Lithology* q);

    LithologyManager* getLithologyManager();

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    LithologyItem* findItemForLithology(int id);

private:
    LithologyItem* appendItem(Lithology* oc);

    Project* _project;
};

#endif	/* _LITHOLOGYITEMMODEL_H */
