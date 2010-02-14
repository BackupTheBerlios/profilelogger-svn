#ifndef _PROJECTVIEW_H
#define	_PROJECTVIEW_H

#include "TreeView.h"

class Project;

class ProjectItemModel;

class ProjectView : public TreeView {
    Q_OBJECT
public:
    ProjectView(QWidget* parent, ProjectItemModel* model);
    virtual ~ProjectView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);

public slots:
    void selectProject(Project* q);
    void slotIndexActivated(const QModelIndex&);
    //    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotEdit();
    void slotDelete();
};

#endif	/* _PROJECTVIEW_H */

