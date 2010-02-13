/*
 * File:   GrainSize.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "GrainSize.h"

GrainSize::GrainSize(int id, int order, const QString& name, 
        const QString& description,
        GraphicColumnHeader::WidthPositions pos)
: Dataset(id, name, description),
_order(order),
_pos(pos) {
    setOrder(order);
}

GrainSize::~GrainSize() {
}

QString GrainSize::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Grain Size:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());
    return ret.join("\n");
}
