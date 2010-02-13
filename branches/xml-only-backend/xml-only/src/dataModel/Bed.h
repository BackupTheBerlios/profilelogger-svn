/* 
 * File:   Bed.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:21
 */

#ifndef _BED_H
#define	_BED_H

#include "Dataset.h"

#include "GrainSizeModes.h"
#include "Fossil.h"
#include "LengthMeasurement.h"

class OutcropQuality;
class Color;
class Lithology;
class BeddingType;
class BoundaryType;
class ClasticGrainSize;
class CarbonateGrainSize;
class Fossil;
class Profile;
class SedimentStructure;
class CustomSymbol;
class Facies;
class LithologicalUnit;

class Bed : public Dataset {
public:


    Bed(Profile* profile = 0,
            int id = 0,
            int position = 0,
            const QString& name = QObject::tr("New Bed"),
            const QString& description = QString::null);

    virtual ~Bed();

    void setPosition(int p);

    int getPosition() const {
        return _position;
    }

    bool hasValidHeight() const;
    qreal getScaledHeight();
    QString getFormattedHeight();
    
    LengthMeasurement* getHeight() const {
        return _height;
    }

    bool hasOutcropQuality() const {
        return 0 != _outcropQuality;
    }

    void setOutcropQuality(OutcropQuality* c) {
        _outcropQuality = c;
    }

    OutcropQuality* getOutcropQuality() const {
        return _outcropQuality;
    }

    QString makeToolTipText(const bool withDatasetName = false) const;

    bool hasFacies() const {
        return 0 != _facies;
    }

    void setFacies(Facies* c) {
        _facies = c;
    }

    Facies* getFacies() const {
        return _facies;
    }

    bool hasLithologicalUnit() const {
        return 0 != _lithologicalUnit;
    }

    void setLithologicalUnit(LithologicalUnit* c) {
        _lithologicalUnit = c;
    }

    LithologicalUnit* getLithologicalUnit() const {
        return _lithologicalUnit;
    }

    bool hasColor() const {
        return 0 != _color;
    }

    void setColor(Color* c) {
        _color = c;
    }

    Color* getColor() const {
        return _color;
    }

    bool hasLithology() const {
        return 0 != _lithology;
    }

    void setLithology(Lithology* c) {
        _lithology = c;
    }

    Lithology* getLithology() const {
        return _lithology;
    }

    bool hasBeddingType() const {
        return 0 != _beddingType;
    }

    void setBeddingType(BeddingType* c) {
        _beddingType = c;
    }

    BeddingType* getBeddingType() const {
        return _beddingType;
    }

    bool hasTopBoundaryType() const {
        return 0 != _topBoundaryType;
    }

    void setTopBoundaryType(BoundaryType* c) {
        _topBoundaryType = c;
    }

    BoundaryType* getTopBoundaryType() const {
        return _topBoundaryType;
    }

    void setGrainSizeMode(GrainSizeModes m) {
        _grainSizeMode = m;
    }

    GrainSizeModes getGrainSizeMode() {
        return _grainSizeMode;
    }

    bool hasClasticGrainSizeMode() const {
        return ClasticGrainSizeMode == _grainSizeMode;
    }

    bool hasCarbonateGrainSizeMode() const {
        return CarbonateGrainSizeMode == _grainSizeMode;
    }

    bool hasBaseCarbonateGrainSize() const {
        return 0 != _baseCarbonateGrainSize;
    }

    bool hasTopCarbonateGrainSize() const {
        return 0 != _topCarbonateGrainSize;
    }

    void setBaseCarbonateGrainSize(CarbonateGrainSize* c) {
        _baseCarbonateGrainSize = c;
    }

    void setTopCarbonateGrainSize(CarbonateGrainSize* c) {
        _topCarbonateGrainSize = c;
    }

    CarbonateGrainSize* getBaseCarbonateGrainSize() const {
        return _baseCarbonateGrainSize;
    }

    CarbonateGrainSize* getTopCarbonateGrainSize() const {
        return _topCarbonateGrainSize;
    }

    bool hasBaseClasticGrainSize() const {
        return 0 != _baseClasticGrainSize;
    }

    bool hasTopClasticGrainSize() const {
        return 0 != _topClasticGrainSize;
    }

    void setBaseClasticGrainSize(ClasticGrainSize* c) {
        _baseClasticGrainSize = c;
    }

    void setTopClasticGrainSize(ClasticGrainSize* c) {
        _topClasticGrainSize = c;
    }

    ClasticGrainSize* getBaseClasticGrainSize() const {
        return _baseClasticGrainSize;
    }

    ClasticGrainSize* getTopClasticGrainSize() const {
        return _topClasticGrainSize;
    }

    int getFossilCount() const;

    void addFossils(QList<Fossil*> fossils) {
        for (QList<Fossil*>::iterator it = fossils.begin(); it != fossils.end(); it++) {
            addFossil(*it);
        }
    }

    void removeFossils(QList<Fossil*> fossils) {
        for (QList<Fossil*>::iterator it = fossils.begin(); it != fossils.end(); it++) {
            removeFossil(*it);
        }
    }

    void addFossil(Fossil* s) {
        _fossils.append(s);
    }

    void removeFossil(Fossil* s) {
        if (_fossils.contains(s)) {
            _fossils.removeAll(s);
        }
    }

    QList<Fossil*>::iterator getFirstFossil() {
        return _fossils.begin();
    }

    QList<Fossil*>::iterator getLastFossil() {
        return _fossils.end();
    }

    void addSedimentStructures(QList<SedimentStructure*> sedimentStructures) {
        for (QList<SedimentStructure*>::iterator it = sedimentStructures.begin(); it != sedimentStructures.end(); it++) {
            addSedimentStructure(*it);
        }
    }

    void removeSedimentStructures(QList<SedimentStructure*> sedimentStructures) {
        for (QList<SedimentStructure*>::iterator it = sedimentStructures.begin(); it != sedimentStructures.end(); it++) {
            removeSedimentStructure(*it);
        }
    }

    void addSedimentStructure(SedimentStructure* s) {
        _sedimentStructures.append(s);
    }

    void removeSedimentStructure(SedimentStructure* s) {
        if (_sedimentStructures.contains(s)) {
            _sedimentStructures.removeAll(s);
        }
    }

    int getSedimentStructureCount() const;

    QList<SedimentStructure*>::iterator getFirstSedimentStructure() {
        return _sedimentStructures.begin();
    }

    QList<SedimentStructure*>::iterator getLastSedimentStructure() {
        return _sedimentStructures.end();
    }

    int getCustomSymbolCount() const;

    void addCustomSymbols(QList<CustomSymbol*> customSymbols) {
        for (QList<CustomSymbol*>::iterator it = customSymbols.begin(); it != customSymbols.end(); it++) {
            addCustomSymbol(*it);
        }
    }

    void removeCustomSymbols(QList<CustomSymbol*> customSymbols) {
        for (QList<CustomSymbol*>::iterator it = customSymbols.begin(); it != customSymbols.end(); it++) {
            removeCustomSymbol(*it);
        }
    }

    void addCustomSymbol(CustomSymbol* s) {
        _customSymbols.append(s);
    }

    void removeCustomSymbol(CustomSymbol* s) {
        if (_customSymbols.contains(s)) {
            _customSymbols.removeAll(s);
        }
    }

    QList<CustomSymbol*>::iterator getFirstCustomSymbol() {
        return _customSymbols.begin();
    }

    QList<CustomSymbol*>::iterator getLastCustomSymbol() {
        return _customSymbols.end();
    }

    Profile* getProfile() {
        return _profile;
    }

    bool hasProfile() const {
      return (0 != _profile);
    }

private:
    Profile* _profile;
    int _position;
    LengthMeasurement* _height;

    OutcropQuality* _outcropQuality;
    Color* _color;
    Lithology* _lithology;
    BeddingType* _beddingType;
    BoundaryType* _topBoundaryType;
    GrainSizeModes _grainSizeMode;
    ClasticGrainSize* _baseClasticGrainSize;
    ClasticGrainSize* _topClasticGrainSize;
    CarbonateGrainSize* _baseCarbonateGrainSize;
    CarbonateGrainSize* _topCarbonateGrainSize;
    Facies* _facies;
    LithologicalUnit* _lithologicalUnit;
    
    QList<Fossil*> _fossils;
    QList<SedimentStructure*> _sedimentStructures;
    QList<CustomSymbol*> _customSymbols;
};

#endif	/* _BED_H */

