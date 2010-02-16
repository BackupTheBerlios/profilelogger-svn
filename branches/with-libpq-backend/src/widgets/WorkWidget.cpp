/* 
 * File:   WorkWidget.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:15
 */

#include "WorkWidget.h"

#include <QApplication>
#include <QLayout>
#include <QSplitter>
#include <QTabWidget>
#include <QAction>

#include "ProfileItemModel.h"
#include "ProfileItemView.h"
#include "BedItemModel.h"
#include "BedItemView.h"
#include "SampleItemModel.h"
#include "SampleItemView.h"
#include "ImageItemModel.h"
#include "ImageItemView.h"

#include "ManagementToolBox.h"
#include "ProfileLogger.h"
#include "GraphicColumnWidget.h"

WorkWidget::WorkWidget(QWidget* p)
: QWidget(p) {
    _profilesM = (static_cast<ProfileLogger*> (QApplication::instance()))->getProfileItemModel();
    _bedsM = (static_cast<ProfileLogger*> (QApplication::instance()))->getBedItemModel();
    _samplesM = (static_cast<ProfileLogger*> (QApplication::instance()))->getSampleItemModel();
    //_imagesM = (static_cast<ProfileLogger*> (QApplication::instance()))->getImageItemModel();

    _splitterW = new QSplitter(this);

    _profilesV = new ProfileItemView(_splitterW, _profilesM);
    _bedSamplesTabW = new QTabWidget(_splitterW);
    _bedsV = new BedItemView(_bedSamplesTabW, _bedsM);
    _samplesV = new SampleItemView(_bedSamplesTabW, _samplesM);
    //    _imagesV = new ImageItemView(_bedSamplesTabW, _imagesM);
    _columnW = new GraphicColumnWidget(_splitterW);
    //_columnW->setSizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::MinimumExpanding);

    _bedSamplesTabW->addTab(_bedsV, tr("Beds"));
    _bedSamplesTabW->addTab(_samplesV, tr("Samples"));
    //    _bedSamplesTabW->addTab(_imagesV, tr("Images"));
    
    _managementW = new ManagementToolBox(_splitterW);

    setLayout(new QHBoxLayout(this));
    layout()->addWidget(_splitterW);

    _splitterW->addWidget(_profilesV);
    _splitterW->addWidget(_columnW);
    _splitterW->addWidget(_bedSamplesTabW);
    _splitterW->addWidget(_managementW);

    setEnabled(false);

    connect((static_cast<ProfileLogger*> (QApplication::instance())), SIGNAL(currentProjectChanged(Project*)), this, SLOT(slotCurrentProjectChanged(Project*)));
    connect(_profilesV, SIGNAL(currentProfileChanged(Profile*)), _bedsM, SLOT(slotCurrentProfileChanged(Profile*)));
    connect(_bedsM, SIGNAL(reloaded()), _columnW, SLOT(reload()));
    connect(_profilesV, SIGNAL(currentProfileChanged(Profile*)), _samplesM, SLOT(slotCurrentProfileChanged(Profile*)));
    connect(_profilesV, SIGNAL(currentProfileChanged(Profile*)), _samplesV, SLOT(slotCurrentProfileChanged(Profile*)));
    connect(_profilesV, SIGNAL(currentProfileChanged(Profile*)), _bedsM, SLOT(slotCurrentProfileChanged(Profile*)));
    connect(_profilesV, SIGNAL(currentProfileChanged(Profile*)), _bedsV, SLOT(slotCurrentProfileChanged(Profile*)));
    //    connect(_profilesV, SIGNAL(currentProfileChanged(Profile*)), _imagesM, SLOT(slotCurrentProfileChanged(Profile*)));
    //    connect(_profilesV, SIGNAL(currentProfileChanged(Profile*)), _imagesV, SLOT(slotCurrentProfileChanged(Profile*)));
    connect(_profilesV, SIGNAL(currentProfileChanged(Profile*)), _columnW, SLOT(slotCurrentProfileChanged(Profile*)));
}

WorkWidget::~WorkWidget() {
}

void WorkWidget::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(0 != _project);
}
