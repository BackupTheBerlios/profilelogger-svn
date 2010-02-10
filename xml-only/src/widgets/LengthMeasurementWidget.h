/* 
 * File:   LengthMeasurementWidget.h
 * Author: jolo
 *
 * Created on 14. Dezember 2009, 16:12
 */

#ifndef _LENGTHMEASUREMENTWIDGET_H
#define	_LENGTHMEASUREMENTWIDGET_H

#include <QGroupBox>

#include <QMap>

#include "LengthMeasurement.h"
#include "LengthUnitsComboBox.h"

class LengthUnit;
class LengthUnitsComboBox;

class QSpinBox;
class QLabel;
class QComboBox;

class LengthMeasurement;

class LengthMeasurementWidget : public QGroupBox {
    Q_OBJECT

public:
    LengthMeasurementWidget(QWidget* p = 0);
    virtual ~LengthMeasurementWidget();

public slots:
    void slotValueChanged(int v);
    void slotUnitChanged(LengthUnit* u);
    void setMeasurement(LengthMeasurement* m);

private:
    QSpinBox* _valueW;
    LengthUnitsComboBox* _unitsW;

    LengthMeasurement* _measurement;
};

#endif	/* _LENGTHMEASUREMENTWIDGET_H */

