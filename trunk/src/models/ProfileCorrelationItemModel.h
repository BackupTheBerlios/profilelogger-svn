/* 
 * File:   ProfileCorrelationItemModel.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:12
 */

#ifndef _PROFILECORRELATIONITEMMODEL_H
#define	_PROFILECORRELATIONITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class ProfileCorrelation;
class ProfileCorrelationItem;

class ProfileCorrelationItemModel : public StandardItemModel {
    Q_OBJECT
public:
    ProfileCorrelationItemModel(QObject* p = 0);
    virtual ~ProfileCorrelationItemModel();

signals:
    void selectItemRequest(const QModelIndex& idx);
    
public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDuplicateRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);
    
protected:
    ProfileCorrelationItem* findItemForProfileCorrelation(int id);
    
private:
    ProfileCorrelationItem* appendItem(ProfileCorrelation* p);

    Project* _project;
};

#endif	/* _PROFILECORRELATIONITEMMODEL_H */

