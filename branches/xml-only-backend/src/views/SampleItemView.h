/*
 * File:   SampleItemView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:40
 */

#ifndef _SAMPLEITEMVIEW_H
#define	_SAMPLEITEMVIEW_H

#include "TreeView.h"

class Profile;
class Sample;
class SampleItemModel;

class SampleItemView : public TreeView {
    Q_OBJECT
public:
    SampleItemView(QWidget* p, SampleItemModel* model);
    virtual ~SampleItemView();

signals:
    void currentSampleChanged(Sample* bed);
    void reloadRequest();
    void createSampleRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void exportToLatexRequest();
    
public slots:
    void slotCurrentProfileChanged(Profile* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotIndexActivated(const QModelIndex&);

    void slotReload();
    void slotCreate();
    void slotEdit();
    void slotDelete();
    void slotReloaded();
    void slotExportToLatex();
    
private:
    Profile* _profile;
};

#endif	/* _SAMPLEITEMVIEW_H */
