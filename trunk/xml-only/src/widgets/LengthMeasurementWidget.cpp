/* 
 * File:   LengthMeasurementWidget.cpp
 * Author: jolo
 * 
 * Created on 14. Dezember 2009, 16:12
 */

#include "LengthMeasurementWidget.h"

#include <QLayout>
#include <QSpinBox>
#include <QComboBox>
#include <QApplication>

#include "ProfileLogger.h"
#include "LengthUnit.h"
#include "Project.h"
#include "LengthUnitsComboBox.h"

LengthMeasurementWidget::LengthMeasurementWidget(QWidget* p)
: QGroupBox(p) {
    setLayout(new QHBoxLayout(this));
    _valueW = new QSpinBox(this);
    _valueW->setMinimum(0);
    _valueW->setMaximum(999999);

    _unitsW = new LengthUnitsComboBox(this);

    layout()->addWidget(_valueW);
    layout()->addWidget(_unitsW);

    connect(_valueW, SIGNAL(valueChanged(int)), this, SLOT(slotValueChanged(int)));
    connect(_unitsW, SIGNAL(lengthUnitChanged(LengthUnit*)), this, SLOT(slotUnitChanged(LengthUnit*)));
}

LengthMeasurementWidget::~LengthMeasurementWidget() {
}

void LengthMeasurementWidget::slotUnitChanged(LengthUnit* u) {
    if (_measurement) {
        _measurement->setUnit(u);
        }
}

void LengthMeasurementWidget::slotValueChanged(int v) {
    if (_measurement) {
        _measurement->setValue(v);
    }
}

void LengthMeasurementWidget::setMeasurement(LengthMeasurement* m) {
    _measurement = m;

    if (!_measurement) {
        return;
    }

    _valueW->setValue(_measurement->getValue());
    _unitsW->setLengthUnit(_measurement->getUnit());
}
