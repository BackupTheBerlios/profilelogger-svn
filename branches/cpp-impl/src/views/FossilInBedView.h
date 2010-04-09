/*
 * File:   FossilInBedView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _FOSSILINBEDVIEW_H
#define	_FOSSILINBEDVIEW_H

#include "TreeView.h"

#include <QList>

class Bed;

class FossilInBedItemModel;
class Fossil;

class FossilInBedView : public TreeView {
    Q_OBJECT
public:
    FossilInBedView(QWidget* parent, FossilInBedItemModel* model);
    virtual ~FossilInBedView();
    QList<Fossil*> getSelectedFossils();
    
signals:
    void reloadRequest();
    void currentFossilChanged(Fossil* f);
    void deleteRequest(QModelIndexList indexes);

public slots:
    void selectFossil(Fossil* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentBedChanged(Bed* b);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotDelete();

private:
    Bed* _bed;
};

#endif	/* _FOSSILINBEDVIEW_H */

