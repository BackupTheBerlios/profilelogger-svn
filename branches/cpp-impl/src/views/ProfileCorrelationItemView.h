/* 
 * File:   ProfileCorrelationItemView.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:13
 */

#ifndef _PROFILECORRELATIONITEMVIEW_H
#define	_PROFILECORRELATIONITEMVIEW_H

#include "TreeView.h"

class Project;
class ProfileCorrelation;
class ProfileCorrelationItemModel;

class ProfileCorrelationItemView : public TreeView {
    Q_OBJECT
public:
    ProfileCorrelationItemView(QWidget* p, ProfileCorrelationItemModel* model);

    virtual ~ProfileCorrelationItemView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void duplicateRequest(const QModelIndex& idx);
    void currentProfileCorrelationChanged(ProfileCorrelation* p);
    
public slots:
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotEdit();
    void slotDelete();
    void slotDuplicate();

private:
    Project* _project;
};

#endif	/* _PROFILECORRELATIONITEMVIEW_H */

