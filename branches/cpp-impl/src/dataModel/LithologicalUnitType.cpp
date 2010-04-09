/* 
 * File:   LithologicalUnitType.cpp
 * Author: jolo
 * 
 * Created on 18. Januar 2010, 16:28
 */

#include "LithologicalUnitType.h"

LithologicalUnitType::LithologicalUnitType(int id, const QString& n, const QString& d)
: Dataset(id, n, d) {
}

LithologicalUnitType::~LithologicalUnitType() {
}

QString LithologicalUnitType::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;

    if (withDatasetName) {
        ret << QObject::tr("Lithological Unit Type");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());

    return ret.join("\n");
}
