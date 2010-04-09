/* 
 * File:   OutcropQualityView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _OUTCROPQUALITYVIEW_H
#define	_OUTCROPQUALITYVIEW_H

#include "TreeView.h"

class Project;

class OutcropQualityItemModel;
class OutcropQuality;

class OutcropQualityView : public TreeView {
    Q_OBJECT
public:
    OutcropQualityView(QWidget* parent, OutcropQualityItemModel* model);
    virtual ~OutcropQualityView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentOutcropQualityChanged(OutcropQuality* p);

public slots:
    void selectOutcropQuality(OutcropQuality* q);
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

#endif	/* _OUTCROPQUALITYVIEW_H */

