/*
 * File:   SedimentStructure.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "SedimentStructure.h"

SedimentStructure::SedimentStructure(int id, const QString& name, 
        const QString& description, const QString& fileName)
: DatasetWithFileName(id, name, description, fileName) {
}

SedimentStructure::~SedimentStructure() {
}

QString SedimentStructure::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("SedimentStructure:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription())
            << QObject::tr("File Name: %1").arg(getFileName());
    return ret.join("\n");
}
