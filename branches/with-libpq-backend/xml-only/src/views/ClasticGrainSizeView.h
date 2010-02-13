/*
 * File:   ClasticGrainSizeView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _CLASTICGRAINSIZEVIEW_H
#define	_CLASTICGRAINSIZEVIEW_H

#include "GrainSizeView.h"

class Project;

class ClasticGrainSizeItemModel;
class ClasticGrainSize;

class ClasticGrainSizeView : public GrainSizeView {
    Q_OBJECT
public:
    ClasticGrainSizeView(QWidget* parent, ClasticGrainSizeItemModel* model);
    virtual ~ClasticGrainSizeView();

signals:
    void reloadRequest();
    void currentClasticGrainSizeChanged(ClasticGrainSize* p);

public slots:
    void selectClasticGrainSize(ClasticGrainSize* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();

private:
    Project* _project;
};

#endif	/* _CLASTICGRAINSIZEVIEW_H */

