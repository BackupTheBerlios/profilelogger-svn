/*
 * File:   LithologicalUnitView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _LITHOLOGICALUNITVIEW_H
#define	_LITHOLOGICALUNITVIEW_H

#include "TreeView.h"

class Project;

class LithologicalUnitItemModel;
class LithologicalUnit;

class LithologicalUnitView : public TreeView {
    Q_OBJECT
public:
    LithologicalUnitView(QWidget* parent, LithologicalUnitItemModel* model);
    virtual ~LithologicalUnitView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentLithologicalUnitChanged(LithologicalUnit* p);

public slots:
    void selectLithologicalUnit(LithologicalUnit* q);
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

#endif	/* _LITHOLOGICALUNITVIEW_H */

