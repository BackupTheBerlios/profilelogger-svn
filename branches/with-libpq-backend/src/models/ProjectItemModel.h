#ifndef _PROJECTITEMMODEL_H
#define	_PROJECTITEMMODEL_H

#include "StandardItemModel.h"

#include <QList>

class Project;
class ProjectItem;
class ProjectManager;

class ProjectItemModel : public StandardItemModel {
    Q_OBJECT
public:
    ProjectItemModel(QObject* p = 0);
    virtual ~ProjectItemModel();
    QModelIndex findIndexForProject(Project* q);
    QList<Project*>::iterator getFirstProject();
    QList<Project*>::iterator getLastProject();

signals:
    void selectItemRequest(const QModelIndex& idx);
    
public slots:
    void reload();
    void createNew();
    void slotEditRequested(const QModelIndex& idx);
    void slotDuplicateRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);
    
    ProjectManager* getProjectManager();

protected:
    ProjectItem* findItemForProject(int id);
    
private:
    ProjectItem* appendItem(Project* p);

    QList<Project*> _projects;
};

#endif	/* _PROJECTITEMMODEL_H */

