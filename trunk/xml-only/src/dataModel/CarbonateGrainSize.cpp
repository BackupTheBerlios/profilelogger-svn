/*
 * File:   GrainSize.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "CarbonateGrainSize.h"

CarbonateGrainSize::CarbonateGrainSize(int id, int order, const QString& name, 
        const QString& description,
        GraphicColumnHeader::WidthPositions pos)
: GrainSize(id, order, name, description, pos) {
    setOrder(order);
}

CarbonateGrainSize::~CarbonateGrainSize() {
}

QString CarbonateGrainSize::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Carbonate Grain Size:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());
    return ret.join("\n");
}
