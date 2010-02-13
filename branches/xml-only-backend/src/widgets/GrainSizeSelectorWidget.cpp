/* 
 * File:   GrainSizeSelectorWidget.cpp
 * Author: jolo
 * 
 * Created on 23. Januar 2010, 13:33
 */

#include "GrainSizeSelectorWidget.h"
#include "ProfileLogger.h"
#include "CarbonateGrainSizeView.h"
#include "ClasticGrainSizeView.h"
#include "GrainSizeModeSelectorWidget.h"

#include <QApplication>
#include <QLayout>

GrainSizeSelectorWidget::GrainSizeSelectorWidget(QWidget* p)
: QWidget(p) {
    setLayout(new QVBoxLayout(this));

    _modesW = new GrainSizeModeSelectorWidget(this);

    QWidget* w = new QWidget(this);
    w->setLayout(new QHBoxLayout(w));

    _carbW = new CarbonateGrainSizeView(w, (static_cast<ProfileLogger*> (QApplication::instance()))->getCarbonateGrainSizeItemModel());
    _clastW = new ClasticGrainSizeView(w, (static_cast<ProfileLogger*> (QApplication::instance()))->getClasticGrainSizeItemModel());

    w->layout()->addWidget(_carbW);
    w->layout()->addWidget(_clastW);

    layout()->addWidget(_modesW);
    layout()->addWidget(w);

    connect(_modesW, SIGNAL(modeChanged(GrainSizeModes)), this, SLOT(slotGrainSizeModeChanged(GrainSizeModes)));
    connect(_carbW, SIGNAL(currentCarbonateGrainSizeChanged(CarbonateGrainSize*)), SLOT(slotCarbonateGrainSizeChanged(CarbonateGrainSize*)));
    connect(_clastW, SIGNAL(currentClasticGrainSizeChanged(ClasticGrainSize*)), SLOT(slotClasticGrainSizeChanged(ClasticGrainSize*)));
}

GrainSizeSelectorWidget::~GrainSizeSelectorWidget() {
}

void GrainSizeSelectorWidget::slotCarbonateGrainSizeChanged(CarbonateGrainSize* s) {
    emit carbonateGrainSizeChanged(s);
}

void GrainSizeSelectorWidget::slotClasticGrainSizeChanged(ClasticGrainSize* s) {
    emit clasticGrainSizeChanged(s);
}

void GrainSizeSelectorWidget::slotGrainSizeModeChanged(GrainSizeModes m) {
    _clastW->setEnabled(false);
    _carbW->setEnabled(false);

    emit grainSizeModeChanged(m);

    switch (m) {
        case(CarbonateGrainSizeMode): {
                _carbW->setEnabled(true);
                _clastW->clearSelection();
                break;
            }
        case(ClasticGrainSizeMode): {
            _clastW->setEnabled(true);
            _carbW->clearSelection();
        }
        default: return;
    }
}

void GrainSizeSelectorWidget::setGrainSizeMode(GrainSizeModes m) {
    _modesW->setMode(m);
    switch(m) {
        case(CarbonateGrainSizeMode): {
            _carbW->setEnabled(true);
            _clastW->setEnabled(false);
            break;
        }
        case(ClasticGrainSizeMode): {
            _clastW->setEnabled(true);
            _carbW->setEnabled(false);
        }
    }
}

void GrainSizeSelectorWidget::setCarbonateGrainSize(CarbonateGrainSize* s) {
    if (s) {
        setGrainSizeMode(CarbonateGrainSizeMode);
        _carbW->selectCarbonateGrainSize(s);
        _clastW->clearSelection();
    }
}

void GrainSizeSelectorWidget::setClasticGrainSize(ClasticGrainSize* s) {
    if (s) {
        setGrainSizeMode(ClasticGrainSizeMode);
        _clastW->selectClasticGrainSize(s);
        _carbW->clearSelection();
    }
}
