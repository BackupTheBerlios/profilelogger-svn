/*
 * File:   LithologyView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _LITHOLOGYVIEW_H
#define	_LITHOLOGYVIEW_H

#include "TreeView.h"

class Project;

class LithologyItemModel;
class Lithology;

class LithologyView : public TreeView {
    Q_OBJECT
public:
    LithologyView(QWidget* parent, LithologyItemModel* model);
    virtual ~LithologyView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentLithologyChanged(Lithology* p);

public slots:
    void selectLithology(Lithology* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotEdit();
    void slotDelete();
    void slotReloaded();

private:
    Project* _project;
};

#endif	/* _LITHOLOGYVIEW_H */

