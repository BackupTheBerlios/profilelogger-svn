/*
 * File:   SedimentStructureView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _SEDIMENTSTRUCTUREVIEW_H
#define	_SEDIMENTSTRUCTUREVIEW_H

#include "TreeView.h"

#include <QList>

class Project;

class SedimentStructureItemModel;
class SedimentStructure;

class SedimentStructureView : public TreeView {
    Q_OBJECT
public:
    SedimentStructureView(QWidget* parent, SedimentStructureItemModel* model);
    virtual ~SedimentStructureView();
    QList<SedimentStructure*> getSelectedSedimentStructures();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentSedimentStructureChanged(SedimentStructure* p);

public slots:
    void selectSedimentStructure(SedimentStructure* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotEdit();
    void slotDelete();

private:
    Project* _project;
};

#endif	/* _SEDIMENTSTRUCTUREVIEW_H */

