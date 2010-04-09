/*
 * File:   FossilView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _FOSSILVIEW_H
#define	_FOSSILVIEW_H

#include "TreeView.h"

class Project;

class FossilItemModel;
class Fossil;

class FossilView : public TreeView {
    Q_OBJECT
public:
    FossilView(QWidget* parent, FossilItemModel* model);
    virtual ~FossilView();

    QList<Fossil*> getSelectedFossils();
    
signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentFossilChanged(Fossil* p);

public slots:
    void selectFossil(Fossil* q);
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

#endif	/* _FOSSILVIEW_H */

