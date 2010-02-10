/* 
 * File:   ProfileItemView.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:13
 */

#ifndef _PROFILEITEMVIEW_H
#define	_PROFILEITEMVIEW_H

#include "TreeView.h"

class Project;
class Profile;
class ProfileItemModel;

class ProfileItemView : public TreeView {
    Q_OBJECT
public:
    ProfileItemView(QWidget* p, ProfileItemModel* model);

    virtual ~ProfileItemView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void duplicateRequest(const QModelIndex& idx);
    void currentProfileChanged(Profile* p);
    void importFromCsvFileRequest(const QModelIndex& idx);
    
public slots:
    void selectProfile(Profile* p);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotEdit();
    void slotDelete();
    void slotDuplicate();
    void slotImportFromCsvFile();

private:
    Project* _project;
};

#endif	/* _PROFILEITEMVIEW_H */

