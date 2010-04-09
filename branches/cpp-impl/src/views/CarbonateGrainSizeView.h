/*
 * File:   CarbonateGrainSizeView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _CARBONATEGRAINSIZEVIEW_H
#define	_CARBONATEGRAINSIZEVIEW_H

#include "GrainSizeView.h"

class Project;

class CarbonateGrainSizeItemModel;
class CarbonateGrainSize;

class CarbonateGrainSizeView : public GrainSizeView {
    Q_OBJECT
public:
    CarbonateGrainSizeView(QWidget* parent, CarbonateGrainSizeItemModel* model);
    virtual ~CarbonateGrainSizeView();

signals:
    void reloadRequest();
    void currentCarbonateGrainSizeChanged(CarbonateGrainSize* p);

public slots:
    void selectCarbonateGrainSize(CarbonateGrainSize* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    
private:
    Project* _project;
};

#endif	/* _CARBONATEGRAINSIZEVIEW_H */

