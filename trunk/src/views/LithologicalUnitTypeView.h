/*
 * File:   LithologicalUnitTypeView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _LITHOLOGICALUNITTYPEVIEW_H
#define	_LITHOLOGICALUNITTYPEVIEW_H

#include "TreeView.h"

class Project;

class LithologicalUnitTypeItemModel;
class LithologicalUnitType;

class LithologicalUnitTypeView : public TreeView {
    Q_OBJECT
public:
    LithologicalUnitTypeView(QWidget* parent, LithologicalUnitTypeItemModel* model);
    virtual ~LithologicalUnitTypeView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentLithologicalUnitTypeChanged(LithologicalUnitType* p);

public slots:
    void selectLithologicalUnitType(LithologicalUnitType* q);
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

#endif	/* _LITHOLOGICALUNITTYPEVIEW_H */

