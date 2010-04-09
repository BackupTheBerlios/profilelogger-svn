/*
 * File:   CustomSymbolInBedView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _CUSTOMSYMBOLINBEDVIEW_H
#define	_CUSTOMSYMBOLINBEDVIEW_H

#include "TreeView.h"

#include <QList>

class Bed;

class CustomSymbolInBedItemModel;
class CustomSymbol;

class CustomSymbolInBedView : public TreeView {
    Q_OBJECT
public:
    CustomSymbolInBedView(QWidget* parent, CustomSymbolInBedItemModel* model);
    virtual ~CustomSymbolInBedView();
    QList<CustomSymbol*> getSelectedCustomSymbols();

signals:
    void reloadRequest();
    void currentCustomSymbolChanged(CustomSymbol* f);
    void deleteRequest(QModelIndexList indexes);

public slots:
    void selectCustomSymbol(CustomSymbol* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentBedChanged(Bed* b);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotDelete();

private:
    Bed* _bed;
};

#endif	/* _CUSTOMSYMBOLINBEDVIEW_H */

