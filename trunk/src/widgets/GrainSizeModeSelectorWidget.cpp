/* 
 * File:   GrainSizeModeSelectorWidget.cpp
 * Author: jolo
 * 
 * Created on 12. Dezember 2009, 18:11
 */

#include "GrainSizeModeSelectorWidget.h"
#include "BedEditorDialog.h"

#include <QLayout>
#include <QRadioButton>
#include <QGroupBox>

GrainSizeModeSelectorWidget::GrainSizeModeSelectorWidget(QWidget* p)
: QGroupBox(p) {
    setLayout(new QHBoxLayout(this));
    setTitle(tr("Grain Size Mode"));
    _carbonateW = new QRadioButton(tr("Carbonates"), this);
    _clasticW = new QRadioButton(tr("Clastic"), this);
    layout()->addWidget(_carbonateW);
    layout()->addWidget(_clasticW);

    connect(_clasticW, SIGNAL(toggled(bool)), this, SLOT(slotClasticToggled(bool)));
    connect(_carbonateW, SIGNAL(toggled(bool)), this, SLOT(slotCarbonateToggled(bool)));
}

GrainSizeModeSelectorWidget::~GrainSizeModeSelectorWidget() {
}

void GrainSizeModeSelectorWidget::slotClasticToggled(bool b) {
    (void) b;
    GrainSizeModes m = ClasticGrainSizeMode;

    if (_clasticW->isChecked()) {
        m = ClasticGrainSizeMode;
    }
    if (_carbonateW->isChecked()) {
        m = CarbonateGrainSizeMode;
    }

    if (_mode != m) {
        _mode = m;
        emit modeChanged(_mode);
    }
}

void GrainSizeModeSelectorWidget::slotCarbonateToggled(bool b) {
    (void) b;
    GrainSizeModes m = ClasticGrainSizeMode;

    if (_clasticW->isChecked()) {
        m = ClasticGrainSizeMode;
    }
    if (_carbonateW->isChecked()) {
        m = CarbonateGrainSizeMode;
    }

    if (_mode != m) {
        _mode = m;
        emit modeChanged(_mode);
    }
}

void GrainSizeModeSelectorWidget::setMode(GrainSizeModes m) {
    _mode = m;
    switch (_mode) {

        case (ClasticGrainSizeMode): {
                _clasticW->setChecked(true);
                break;
            }

        case (CarbonateGrainSizeMode): {
                _carbonateW->setChecked(true);
                break;
            }
        default: break;
    }
}
