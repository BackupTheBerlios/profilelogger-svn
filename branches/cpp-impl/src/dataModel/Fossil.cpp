/*
 * File:   Fossil.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "Fossil.h"

#include <QObject>
#include <QStringList>

Fossil::Fossil(int id, const QString& name, const QString& description, const QString& fileName)
: DatasetWithFileName(id, name, description, fileName) {
}

Fossil::~Fossil() {
}

QString Fossil::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Fossil:");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription())
            << QObject::tr("File: %1").arg(getFileName());
    return ret.join("\n");
}
