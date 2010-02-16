/*
 * File:   Lithology.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#include "Lithology.h"

#include "ClasticGrainSize.h"
#include "CarbonateGrainSize.h"
#include "LithologyEditorDialog.h"

Lithology::Lithology(Project* p,
		     int id,
		     const QString& name,
		     const QString& description, 
		     const QString& fileName,
		     GrainSizeModes defaultGrainSizeMode,
		     ClasticGrainSize* defaultClasticGrainSize,
		     CarbonateGrainSize* defaultCarbonateGrainSize)
  : DatasetInProjectWithFileName(p,
				 id, 
				 name, 
				 description, 
				 fileName),
    _defaultGrainSizeMode(defaultGrainSizeMode),
    _defaultCarbonateGrainSize(defaultCarbonateGrainSize),
    _defaultClasticGrainSize(defaultClasticGrainSize) {
    }

Lithology::~Lithology() {
}

QString Lithology::makeToolTipText(const bool withDatasetName) const {
  QStringList ret;
  if (withDatasetName) {
    ret << QObject::tr("Lithology:");
  }

  ret << QObject::tr("Id: %1").arg(getId())
      << QObject::tr("Name: %1").arg(getName())
      << QObject::tr("Description: %1").arg(getDescription())
      << QObject::tr("Pattern File: %1").arg(getFileName());
  if (CarbonateGrainSizeMode == _defaultGrainSizeMode) {
    ret << QObject::tr("Grain Size Mode: Carbonate Grains");
  }

  if (ClasticGrainSizeMode == _defaultGrainSizeMode) {
    ret << QObject::tr("Grain Size Mode: Clastic Grains");
  }

  if (hasDefaultCarbonateGrainSize()) {
    ret << QObject::tr("Default Carbonate Grain Size: %1").arg(getDefaultCarbonateGrainSize()->getName());
  }

  if (hasDefaultClasticGrainSize()) {
    ret << QObject::tr("Default Clastic Grain Size: %1").arg(getDefaultClasticGrainSize()->getName());
  }
  return ret.join("\n");
}

QString Lithology::getDefaultGrainSizeModeName() {
  switch(getDefaultGrainSizeMode()) {
  case(CarbonateGrainSizeMode): return QObject::tr("Carbonate Grain Size");
  case(ClasticGrainSizeMode): return QObject::tr("Clastic Grain Size");
  default: return QObject::tr("Grain Size Mode Unknown");
  }
}

QString Lithology::getDefaultGrainSizeName() {
  if (hasDefaultCarbonateGrainSize()) {
    return getDefaultCarbonateGrainSize()->getName();
  }
  if (hasDefaultClasticGrainSize()) {
    return getDefaultClasticGrainSize()->getName();
  }

  return QObject::tr("Grain Size Unknown");
}
