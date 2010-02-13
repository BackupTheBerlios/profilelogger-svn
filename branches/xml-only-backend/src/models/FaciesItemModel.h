/*
 * File:   FaciesItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _FACIESITEMMODEL_H
#define	_FACIESITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class Facies;
class FaciesItem;

class FaciesItemModel : public StandardItemModel {
    Q_OBJECT
public:
    FaciesItemModel(QObject* parent = 0);
    virtual ~FaciesItemModel();
    QModelIndex findIndexForFacies(Facies* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    FaciesItem* findItemForFacies(int id);

private:
    FaciesItem* appendItem(Facies* oc);

    Project* _project;
};

#endif	/* _FACIESITEMMODEL_H */
