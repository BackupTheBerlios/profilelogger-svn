/*
 * File:   BeddingTypeView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _BEDDINGTYPEVIEW_H
#define	_BEDDINGTYPEVIEW_H

#include "TreeView.h"

class Project;

class BeddingTypeItemModel;
class BeddingType;

class BeddingTypeView : public TreeView {
    Q_OBJECT
public:
    BeddingTypeView(QWidget* parent, BeddingTypeItemModel* model);
    virtual ~BeddingTypeView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentBeddingTypeChanged(BeddingType* p);

public slots:
    void selectBeddingType(BeddingType* q);
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

#endif	/* _BEDDINGTYPEVIEW_H */

