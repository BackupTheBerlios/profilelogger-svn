/* 
 * File:   OutcropQualityItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#ifndef _OUTCROPQUALITYITEMMODEL_H
#define	_OUTCROPQUALITYITEMMODEL_H

#include "StandardItemModel.h"

class Project;
class OutcropQuality;
class OutcropQualityItem;

class OutcropQualityItemModel : public StandardItemModel {
    Q_OBJECT
public:
    OutcropQualityItemModel(QObject* parent = 0);
    virtual ~OutcropQualityItemModel();
    QModelIndex findIndexForOutcropQuality(OutcropQuality* q);
    
signals:
    void selectItemRequest(const QModelIndex& idx);

public slots:
    void reload();
    void createNew();
    void slotCurrentProjectChanged(Project* p);
    void slotEditRequested(const QModelIndex& idx);
    void slotDeleteRequested(QModelIndexList list);

protected:
    OutcropQualityItem* findItemForOutcropQuality(int id);

private:
    OutcropQualityItem* appendItem(OutcropQuality* oc);

    Project* _project;
};

#endif	/* _OUTCROPQUALITYITEMMODEL_H */
