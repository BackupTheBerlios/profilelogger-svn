/*
 * File:   CustomSymbolInBedItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _CUSTOMSYMBOLINBEDITEMMODEL_H
#define	_CUSTOMSYMBOLINBEDITEMMODEL_H

#include "StandardItemModel.h"

class Bed;
class CustomSymbol;
class CustomSymbolItem;

class CustomSymbolInBedItemModel : public StandardItemModel {
    Q_OBJECT
public:
    CustomSymbolInBedItemModel(QObject* parent = 0);
    virtual ~CustomSymbolInBedItemModel();
    QModelIndex findIndexForCustomSymbol(CustomSymbol* q);

signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void slotCurrentBedChanged(Bed* b);
    void slotDeleteRequested(QModelIndexList list);

protected:
    CustomSymbolItem* findItemForCustomSymbol(int id);

private:
    CustomSymbolItem* appendItem(CustomSymbol* oc);

    Bed* _bed;
};

#endif	/* _CUSTOMSYMBOLINBEDITEMMODEL_H */
