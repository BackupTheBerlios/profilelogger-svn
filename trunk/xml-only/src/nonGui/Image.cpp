/* 
 * File:   Image.cpp
 * Author: jolo
 * 
 * Created on 21. Januar 2010, 07:31
 */

#include "Image.h"

Image::Image(int id,
        const QString& name,
        const QString& description,
        const QString& fileName)
: DatasetWithFileName(id, name, description, fileName) {
}

Image::~Image() {
}

QString Image::makeToolTipText(const bool withDatasetName) {
    QStringList ret;

    if (withDatasetName) {
        ret << QObject::tr("Image");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription())
            << QObject::tr("File Name: %1").arg(getFileName());

    return ret.join("\n");
}
