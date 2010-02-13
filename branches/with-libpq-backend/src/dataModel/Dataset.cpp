/* 
 * File:   Dataset.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 19:41
 */

#include "Dataset.h"

#include <QObject>
#include <QStringList>

Dataset::Dataset(int id,
        const QString& name,
        const QString& description)
  : PrimitiveDataset(id),
_name(name),
_description(description) {
}

Dataset::~Dataset() {
}

QString Dataset::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Dataset:");
    }

    ret << QObject::tr("ID: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());
    return ret.join("\n");
}

void Dataset::copyData(Dataset* other) {
  setName(other->getName());
  setDescription(other->getDescription());
}
