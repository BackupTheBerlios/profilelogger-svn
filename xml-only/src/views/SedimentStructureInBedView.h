/*
 * File:   SedimentStructureInBedView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _SEDIMENTSTRUCTUREINBEDVIEW_H
#define	_SEDIMENTSTRUCTUREINBEDVIEW_H

#include "TreeView.h"

#include <QList>

class Bed;

class SedimentStructureInBedItemModel;
class SedimentStructure;

class SedimentStructureInBedView : public TreeView {
    Q_OBJECT
public:
    SedimentStructureInBedView(QWidget* parent, SedimentStructureInBedItemModel* model);
    virtual ~SedimentStructureInBedView();
    QList<SedimentStructure*> getSelectedSedimentStructures();

signals:
    void reloadRequest();
    void currentSedimentStructureChanged(SedimentStructure* f);
    void deleteRequest(QModelIndexList indexes);

public slots:
    void selectSedimentStructure(SedimentStructure* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentBedChanged(Bed* b);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotDelete();

private:
    Bed* _bed;
};

#endif	/* _SEDIMENTSTRUCTUREINBEDVIEW_H */

