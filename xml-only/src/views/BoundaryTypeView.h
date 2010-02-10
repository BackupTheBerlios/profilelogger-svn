/*
 * File:   BoundaryTypeView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _BOUNDARYTYPEVIEW_H
#define	_BOUNDARYTYPEVIEW_H

#include "TreeView.h"

class Project;

class BoundaryTypeItemModel;
class BoundaryType;

class BoundaryTypeView : public TreeView {
    Q_OBJECT
public:
    BoundaryTypeView(QWidget* parent, BoundaryTypeItemModel* model);
    virtual ~BoundaryTypeView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentBoundaryTypeChanged(BoundaryType* p);

public slots:
    void selectBoundaryType(BoundaryType* q);
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

#endif	/* _BOUNDARYTYPEVIEW_H */

