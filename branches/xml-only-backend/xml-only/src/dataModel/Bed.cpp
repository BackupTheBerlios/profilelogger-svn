/* 
 * File:   Bed.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 11:21
 */

#include "Bed.h"

#include <QApplication>

#include "OutcropQuality.h"
#include "Color.h"
#include "Lithology.h"
#include "BeddingType.h"
#include "BoundaryType.h"
#include "CarbonateGrainSize.h"
#include "ClasticGrainSize.h"
#include "LengthUnit.h"
#include "Project.h"
#include "ProfileLogger.h"
#include "Facies.h"
#include "LithologicalUnit.h"
#include "Profile.h"

Bed::Bed(Profile* profile,
        int id,
        int position,
        const QString& name,
        const QString& description)
: Dataset(id, name, description),
_profile(profile),
_position(position),
_height(0),
_outcropQuality(0),
_color(0),
_lithology(0),
_beddingType(0),
_topBoundaryType(0),
_grainSizeMode(ClasticGrainSizeMode),
_baseClasticGrainSize(0),
_topClasticGrainSize(0),
_baseCarbonateGrainSize(0),
_topCarbonateGrainSize(0),
_facies(0),
_lithologicalUnit(0) {
    setPosition(position);
    _height = new LengthMeasurement(0, 0);
}

Bed::~Bed() {
    delete _height;
}

void Bed::setPosition(int pos) {
    _position = pos;

    setName(QString::number(pos));
}

QString Bed::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << QObject::tr("Bed:");
    }
    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Height: %1").arg(getHeight()->toString())
            << QObject::tr("Bed Number (Position): %1").arg(getPosition())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());

    if (hasOutcropQuality()) {
        ret << getOutcropQuality()->toString(false);
    }

    if (hasColor()) {
        ret << QObject::tr("Color: %1").arg(getColor()->getName());
    }

    if (hasFacies()) {
        ret << QObject::tr("Facies: %1").arg(getFacies()->getName());
    }

    if (hasLithologicalUnit()) {
        ret << QObject::tr("LithologicalUnit: %1").arg(getLithologicalUnit()->getName());
    }

    if (hasLithology()) {
        ret << QObject::tr("Lithology: %1").arg(getLithology()->getName());
    }

    if (hasBeddingType()) {
        ret << QObject::tr("Bedding Type: %1").arg(getBeddingType()->getName());
    }

    if (hasTopBoundaryType()) {
        ret << QObject::tr("Top Boundary Type: %1").arg(getTopBoundaryType()->getName());
    }

    if (hasBaseCarbonateGrainSize()) {
        ret << QObject::tr("Base Carbonate Grain Size: %1").arg(getBaseCarbonateGrainSize()->getName());
    }

    if (hasTopCarbonateGrainSize()) {
        ret << QObject::tr("Top Carbonate Grain Size: %1").arg(getTopCarbonateGrainSize()->getName());
    }


    if (hasBaseClasticGrainSize()) {
        ret << QObject::tr("Base Clastic Grain Size: %1").arg(getBaseClasticGrainSize()->getName());
    }

    if (hasTopClasticGrainSize()) {
        ret << QObject::tr("Top Clastic Grain Size: %1").arg(getTopClasticGrainSize()->getName());
    }

    ret << QObject::tr("Fossil count: %1").arg(_fossils.count());
    ret << QObject::tr("Sediment Structure count: %1").arg(_sedimentStructures.count());
    ret << QObject::tr("Custom Symbol count: %1").arg(_customSymbols.count());

    return ret.join("\n");
}

bool Bed::hasValidHeight() const {
    return (_height->getValue() > 0 && _height->hasUnit());
}

int Bed::getFossilCount() const {
    return _fossils.size();
}

int Bed::getSedimentStructureCount() const {
    return _sedimentStructures.size();
}

int Bed::getCustomSymbolCount() const {
    return _customSymbols.size();
}

qreal Bed::getScaledHeight() {
    return getHeight()->getMillimetres() * _profile->getScaleFactor();
}

QString Bed::getFormattedHeight() {
    if (!hasValidHeight()) {
        return QObject::tr("invalid height");
    }

    QStringList ret;

    ret << QString::number(getHeight()->getValue())
            << getHeight()->getUnit()->getName();
    return ret.join(" ");
}
