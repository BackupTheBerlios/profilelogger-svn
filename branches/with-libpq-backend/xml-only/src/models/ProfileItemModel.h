/* 
 * File:   ProfileItemModel.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:12
 */

#ifndef _PROFILEITEMMODEL_H
#define	_PROFILEITEMMODEL_H

#include "StandardItemModel.h"
#include "CsvProfileImportSettings.h"

class Project;
class Profile;
class ProfileItem;

class ProfileItemModel : public StandardItemModel {
    Q_OBJECT
public:
    ProfileItemModel(QObject* p = 0);
    virtual ~ProfileItemModel();
    QModelIndex findIndexForProfile(Profile* q);

signals:
    void selectItemRequest(const QModelIndex& idx);
    
public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDuplicateRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);
    void slotImportFromCsvFileRequested(const QModelIndex& idx);
    
protected:
    ProfileItem* findItemForProfile(int id);
    
private:
    ProfileItem* appendItem(Profile* p);

    Project* _project;
};

#endif	/* _PROFILEITEMMODEL_H */

