/* 
 * File:   LengthMeasurement.cpp
 * Author: jolo
 * 
 * Created on 14. Dezember 2009, 16:18
 */

#include "LengthMeasurement.h"

#include "LengthUnit.h"

LengthMeasurement::LengthMeasurement(int v, LengthUnit* u)
: _value(v),
_unit(u) {
}

LengthMeasurement::~LengthMeasurement() {
}

QString LengthMeasurement::toString() const {
    if (hasUnit()) {
        return QString("%1 %2").arg(getValue()).arg(getUnit()->getName());
    }
    return QString::number(getValue());
}

int LengthMeasurement::getMillimetres() const {
    if (hasUnit()) {
        return getValue() * getUnit()->getMilliMetre();
    }
    return 0;
}
