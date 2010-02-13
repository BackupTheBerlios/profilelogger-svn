/*
 * File:   Facies.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "Facies.h"
#include "DatasetWithFileName.h"

Facies::Facies(int id, const QString& name, const QString& description,
        const QString& fileName)
: DatasetWithFileName(id, name, description, fileName) {
}

Facies::~Facies() {
}

QString Facies::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Facies:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription())
            << QObject::tr("File Name: %1").arg(getFileName());
    return ret.join("\n");
}
