/*
 * File:   GrainSizeView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _GRAINSIZEVIEW_H
#define	_GRAINSIZEVIEW_H

#include "TreeView.h"

class Project;

class GrainSize;

class GrainSizeView : public TreeView {
    Q_OBJECT
public:
    GrainSizeView(QWidget* parent);
    virtual ~GrainSizeView();

signals:
    void reloadRequest();
    void currentGrainSizeChanged(GrainSize* p);

public slots:
    void selectGrainSize(GrainSize* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    
private:
    Project* _project;
};

#endif	/* _GRAINSIZEVIEW_H */

