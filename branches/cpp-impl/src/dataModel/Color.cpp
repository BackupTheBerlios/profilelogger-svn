/*
 * File:   Color.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "Color.h"

#include <QStringList>

Color::Color(int id, const QString& name, const QString& description, Qt::BrushStyle s)
: Dataset(id, name, description),
_style(s) {
}

Color::~Color() {
}

QString Color::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Color:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());
    return ret.join("\n");
}
