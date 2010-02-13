/*
 * File:   FaciesView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _FACIESVIEW_H
#define	_FACIESVIEW_H

#include "TreeView.h"

class Project;

class FaciesItemModel;
class Facies;

class FaciesView : public TreeView {
    Q_OBJECT
public:
    FaciesView(QWidget* parent, FaciesItemModel* model);
    virtual ~FaciesView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentFaciesChanged(Facies* p);

public slots:
    void selectFacies(Facies* q);
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

#endif	/* _FACIESVIEW_H */

