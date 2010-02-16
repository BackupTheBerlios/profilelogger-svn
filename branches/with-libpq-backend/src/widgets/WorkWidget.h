/* 
 * File:   WorkWidget.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:15
 */

#ifndef _WORKWIDGET_H
#define	_WORKWIDGET_H

#include <QWidget>

class QSplitter;
class QGraphicsView;

class ProfileItemModel;
class BedItemModel;
class ProfileItemView;
class BedItemView;
class ManagementToolBox;
class ColumnView;
class GraphicColumnWidget;
class SampleItemModel;
class SampleItemView;
//class ImageItemModel;
//class ImageItemView;

class Project;

class QTabWidget;

class WorkWidget: public QWidget {
    Q_OBJECT
public:
    WorkWidget(QWidget* p = 0);
    virtual ~WorkWidget();

public slots:
    virtual void slotCurrentProjectChanged(Project* p);

private:
    QSplitter* _splitterW;

    ProfileItemModel* _profilesM;
    ProfileItemView* _profilesV;
    BedItemModel* _bedsM;
    BedItemView* _bedsV;
    SampleItemModel* _samplesM;
    SampleItemView* _samplesV;
    //    ImageItemModel* _imagesM;
    //    ImageItemView* _imagesV;

    ManagementToolBox* _managementW;
    GraphicColumnWidget* _columnW;
    QTabWidget* _bedSamplesTabW;
    
    Project* _project;
};

#endif	/* _WORKWIDGET_H */

