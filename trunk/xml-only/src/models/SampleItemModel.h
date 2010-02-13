/*
 * File:   SampleItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:39
 */

#ifndef _SAMPLEITEMMODEL_H
#define	_SAMPLEITEMMODEL_H

#include "StandardItemModel.h"

class Profile;
class Sample;
class SampleItem;

class SampleItemModel : public StandardItemModel {
    Q_OBJECT
public:
    SampleItemModel(QObject* p = 0);
    virtual ~SampleItemModel();

signals:
    void selectRequest(const QModelIndex& idx);

public slots:
    void slotCurrentProfileChanged(Profile* p);
    void reload();

    void slotCreate();
    void slotEdit(const QModelIndex& idx);
    void slotDelete(QModelIndexList lst);
    void slotExportToLatex();
    
private:
    SampleItem* appendItem(Sample* b);
    SampleItem* findItemForSample(Sample* b);

    Profile* _profile;
};

#endif	/* _SAMPLEITEMMODEL_H */

