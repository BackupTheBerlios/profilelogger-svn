/*
 * File:   BoundaryType.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "BoundaryType.h"

BoundaryType::BoundaryType(Project* p,
			   int id, 
			   const QString& name, 
			   const QString& description, 
			   const QString& fileName)
  : DatasetWithFileName(p,
			id, 
			name,
			description, 
			fileName) {
}

BoundaryType::~BoundaryType() {
}

QString BoundaryType::makeToolTipText(const bool withDatasetName) const {
  QStringList ret;
  if (withDatasetName) {
    ret << QObject::tr("Boundary Type:");
  }

  ret << QObject::tr("Id: %1").arg(getId())
      << QObject::tr("Name: %1").arg(getName())
      << QObject::tr("Description: %1").arg(getDescription())
      << QObject::tr("File Name: %1").arg(getFileName());
  return ret.join("\n");
}
