/*
 * File:   CustomSymbol.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "CustomSymbol.h"

CustomSymbol::CustomSymbol(Project* p,
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

CustomSymbol::~CustomSymbol() {
}

QString CustomSymbol::makeToolTipText(const bool withDatasetName) const {
  QStringList ret;
  if (withDatasetName) {
    ret << QObject::tr("Custom Symbol:");
  }

  ret << QObject::tr("Id: %1").arg(getId())
      << QObject::tr("Name: %1").arg(getName())
      << QObject::tr("Description: %1").arg(getDescription())
      << QObject::tr("File Name: %1").arg(getFileName());
  return ret.join("\n");
}
