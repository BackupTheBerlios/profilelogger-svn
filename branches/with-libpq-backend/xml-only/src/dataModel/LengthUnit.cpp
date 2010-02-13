/*
 * File:   LengthUnit.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "LengthUnit.h"

LengthUnit::LengthUnit(int id, int mm, const QString& name, const QString& description)
: Dataset(id, name, description),
_mm(mm) {
    setMilliMetre(mm);
}

LengthUnit::~LengthUnit() {
}

QString LengthUnit::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Length Unit:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());
    return ret.join("\n");
}
