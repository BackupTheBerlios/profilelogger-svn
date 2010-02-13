/*
 * File:   BeddingType.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "BeddingType.h"

#include <QStringList>

BeddingType::BeddingType(int id, const QString& name, 
        const QString& description, const QString& fileName)
: DatasetWithFileName(id, name, description, fileName) {
}

BeddingType::~BeddingType() {
}

QString BeddingType::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Bedding Type:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription())
            << QObject::tr("File: %1").arg(getFileName());
    return ret.join("\n");
}
