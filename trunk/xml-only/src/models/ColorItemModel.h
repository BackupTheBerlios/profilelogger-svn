/*
 * File:   ColorItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _COLORITEMMODEL_H
#define	_COLORITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class Color;
class ColorItem;

class ColorItemModel : public StandardItemModel {
    Q_OBJECT
public:
    ColorItemModel(QObject* parent = 0);
    virtual ~ColorItemModel();
    QModelIndex findIndexForColor(Color* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    ColorItem* findItemForColor(int id);

private:
    ColorItem* appendItem(Color* oc);

    Project* _project;
};

#endif	/* _COLORITEMMODEL_H */
