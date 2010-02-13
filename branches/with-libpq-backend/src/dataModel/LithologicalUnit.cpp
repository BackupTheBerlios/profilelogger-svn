/* 
 * File:   LithologicalUnit.cpp
 * Author: jolo
 * 
 * Created on 18. Januar 2010, 17:15
 */

#include "LithologicalUnit.h"

#include "LithologicalUnitType.h"

LithologicalUnit::LithologicalUnit(int id, const QString& n, const QString& d,
        LithologicalUnitType* t)
: Dataset(id, n, d),
_lithologicalUnitType(t) {
}

LithologicalUnit::~LithologicalUnit() {
}

QString LithologicalUnit::makeToolTipText(const bool withDatasetName) {
    QStringList ret;

    if (withDatasetName) {
        ret << QObject::tr("Lithological Unit");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());

    if (hasLithologicalUnitType()) {
        ret << QObject::tr("Type: %1").arg(getLithologicalUnitType()->makeToolTipText(false));
    } else {
        ret << QObject::tr("Type: not set");
    }
    
    return ret.join("\n");
}
