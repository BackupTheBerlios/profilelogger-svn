/*
 * File:   CustomSymbolItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _CUSTOMSYMBOLITEMMODEL_H
#define	_CUSTOMSYMBOLITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class CustomSymbol;
class CustomSymbolItem;

class CustomSymbolItemModel : public StandardItemModel {
    Q_OBJECT
public:
    CustomSymbolItemModel(QObject* parent = 0);
    virtual ~CustomSymbolItemModel();
    QModelIndex findIndexForCustomSymbol(CustomSymbol* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    CustomSymbolItem* findItemForCustomSymbol(int id);

private:
    CustomSymbolItem* appendItem(CustomSymbol* oc);

    Project* _project;
};

#endif	/* _CUSTOMSYMBOLITEMMODEL_H */
