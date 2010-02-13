/*
 * File:   GrainSize.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "ClasticGrainSize.h"

ClasticGrainSize::ClasticGrainSize(int id, int order, const QString& name, 
        const QString& description,
        GraphicColumnHeader::WidthPositions pos)
: GrainSize(id, order, name, description, pos) {
    setOrder(order);
}

ClasticGrainSize::~ClasticGrainSize() {
}

QString ClasticGrainSize::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Clastic Grain Size:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());
    return ret.join("\n");
}
