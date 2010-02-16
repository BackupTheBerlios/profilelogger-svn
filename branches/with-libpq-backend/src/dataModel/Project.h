/* 
 * File:   Project.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 19:39
 */

#ifndef _PROJECT_H
#define	_PROJECT_H

#include <QDir>
#include <QString>
#include <QMap>
#include <QMapIterator>
#include <QList>

#include "Dataset.h"
#include "GraphicBedItem.h"
#include "GraphicColumnHeader.h"

class Profile;
class ProfileCorrelation;
class OutcropQuality;
class Color;
class Lithology;
class BeddingType;
class BoundaryType;
class CarbonateGrainSize;
class ClasticGrainSize;
class Fossil;
class SedimentStructure;
class CustomSymbol;
class LengthUnit;
class Facies;
class LithologicalUnitType;
class LithologicalUnit;

class Project: public Dataset {
 public:
  Project(const int id = 0,
	  const QString& name = tr("New Project"),
	  const QString& description = QString::null,
	  const QString& path = QString::null);
  virtual ~Project();

  void setPath(const QString& p) {
    _path = p;
  }

  QString getPath() const {
    return _path;
  }

  Profile* duplicateProfile(Profile* p);
  Profile* createProfile();
  void deleteProfile(Profile* p);
  Profile* getProfile(int id);

  QList<Profile*>::iterator getFirstProfile() {
    return _profiles.begin();
  }

  QList<Profile*>::iterator getLastProfile() {
    return _profiles.end();
  }

  ProfileCorrelation* duplicateProfileCorrelation(ProfileCorrelation* p);
  ProfileCorrelation* createProfileCorrelation();
  void deleteProfileCorrelation(ProfileCorrelation* p);
  ProfileCorrelation* getProfileCorrelation(int id);

  QList<ProfileCorrelation*>::iterator getFirstProfileCorrelation() {
    return _profileCorrelations.begin();
  }

  QList<ProfileCorrelation*>::iterator getLastProfileCorrelation() {
    return _profileCorrelations.end();
  }

  OutcropQuality* createOutcropQuality();
  void deleteOutcropQuality(OutcropQuality* oq);
  OutcropQuality* getOutcropQuality(int id);

  int getOutcropQualityCount() {
    return _outcropQualities.size();
  }

  QList<OutcropQuality*>::iterator getFirstOutcropQuality() {
    return _outcropQualities.begin();
  }

  QList<OutcropQuality*>::iterator getLastOutcropQuality() {
    return _outcropQualities.end();
  }

  Color* createColor();
  void deleteColor(Color* oq);
  Color* getColor(int id);

  int getColorCount() {
    return _colors.size();
  }

  QList<Color*>::iterator getFirstColor() {
    return _colors.begin();
  }

  QList<Color*>::iterator getLastColor() {
    return _colors.end();
  }

  LithologicalUnitType* createLithologicalUnitType();
  void deleteLithologicalUnitType(LithologicalUnitType* oq);
  LithologicalUnitType* getLithologicalUnitType(int id);

  int getLithologicalUnitTypeCount() {
    return _lithologicalUnitTypes.size();
  }

  QList<LithologicalUnitType*>::iterator getFirstLithologicalUnitType() {
    return _lithologicalUnitTypes.begin();
  }

  QList<LithologicalUnitType*>::iterator getLastLithologicalUnitType() {
    return _lithologicalUnitTypes.end();
  }

  LithologicalUnit* createLithologicalUnit();
  void deleteLithologicalUnit(LithologicalUnit* oq);
  LithologicalUnit* getLithologicalUnit(int id);

  int getLithologicalUnitCount() {
    return _lithologicalUnits.size();
  }

  QList<LithologicalUnit*>::iterator getFirstLithologicalUnit() {
    return _lithologicalUnits.begin();
  }

  QList<LithologicalUnit*>::iterator getLastLithologicalUnit() {
    return _lithologicalUnits.end();
  }

  void setLithologies(QList<Lithology*> l) {
    _lithologies = l;
  }

  int getLithologyCount() {
    return _lithologies.size();
  }

  Lithology* createLithology();
  void deleteLithology(Lithology* oq);
  Lithology* getLithology(int id);

  QList<Lithology*>::iterator getFirstLithology() {
    return _lithologies.begin();
  }

  QList<Lithology*>::iterator getLastLithology() {
    return _lithologies.end();
  }

  BeddingType* createBeddingType();
  void deleteBeddingType(BeddingType* oq);
  BeddingType* getBeddingType(int id);

  int getBeddingTypeCount() {
    return _beddingTypes.size();
  }

  QList<BeddingType*>::iterator getFirstBeddingType() {
    return _beddingTypes.begin();
  }

  QList<BeddingType*>::iterator getLastBeddingType() {
    return _beddingTypes.end();
  }

  Facies* createFacies();
  void deleteFacies(Facies* oq);
  Facies* getFacies(int id);

  int getFaciesCount() {
    return _facies.size();
  }

  QList<Facies*>::iterator getFirstFacies() {
    return _facies.begin();
  }

  QList<Facies*>::iterator getLastFacies() {
    return _facies.end();
  }

  BoundaryType* createBoundaryType();
  void deleteBoundaryType(BoundaryType* oq);
  BoundaryType* getBoundaryType(int id);

  int getBoundaryTypeCount() {
    return _boundaryTypes.size();
  }

  QList<BoundaryType*>::iterator getFirstBoundaryType() {
    return _boundaryTypes.begin();
  }

  QList<BoundaryType*>::iterator getLastBoundaryType() {
    return _boundaryTypes.end();
  }

  ClasticGrainSize* getClasticGrainSize(int id);

  QList<ClasticGrainSize*>::iterator getFirstClasticGrainSize() {
    return _clasticGrainSizes.begin();
  }

  QList<ClasticGrainSize*>::iterator getLastClasticGrainSize() {
    return _clasticGrainSizes.end();
  }

  CarbonateGrainSize* getCarbonateGrainSize(int id);

  QList<CarbonateGrainSize*>::iterator getFirstCarbonateGrainSize() {
    return _carbonateGrainSizes.begin();
  }

  QList<CarbonateGrainSize*>::iterator getLastCarbonateGrainSize() {
    return _carbonateGrainSizes.end();
  }

  Fossil* createFossil();
  void deleteFossil(Fossil* oq);
  Fossil* getFossil(int id);

  int getFossilCount() {
    return _fossils.size();
  }

  QList<Fossil*>::iterator getFirstFossil() {
    return _fossils.begin();
  }

  QList<Fossil*>::iterator getLastFossil() {
    return _fossils.end();
  }

  SedimentStructure* createSedimentStructure();
  void deleteSedimentStructure(SedimentStructure* oq);
  SedimentStructure* getSedimentStructure(int id);

  int getSedimentStructureCount() {
    return _sedimentStructures.size();
  }

  QList<SedimentStructure*>::iterator getFirstSedimentStructure() {
    return _sedimentStructures.begin();
  }

  QList<SedimentStructure*>::iterator getLastSedimentStructure() {
    return _sedimentStructures.end();
  }

  CustomSymbol* createCustomSymbol();
  void deleteCustomSymbol(CustomSymbol* oq);
  CustomSymbol* getCustomSymbol(int id);

  int getCustomSymbolCount() {
    return _customSymbols.size();
  }

  QList<CustomSymbol*>::iterator getFirstCustomSymbol() {
    return _customSymbols.begin();
  }

  QList<CustomSymbol*>::iterator getLastCustomSymbol() {
    return _customSymbols.end();
  }

  LengthUnit* getDefaultLengthUnit();

  LengthUnit* getLengthUnit(int id);

  QList<LengthUnit*>::iterator getFirstLengthUnit() {
    return _lengthUnits.begin();
  }

  QList<LengthUnit*>::iterator getLastLengthUnit() {
    return _lengthUnits.end();
  }
 protected:
  virtual void setupGrainSizes();
  virtual void setupCarbonateGrainSizes();
  virtual void setupClasticGrainSizes();
  virtual void setupLengthUnits();

  ClasticGrainSize* createClasticGrainSize(int order,
					   const QString& name,
					   const QString& description,
					   GraphicColumnHeader::WidthPositions pos);
  void deleteClasticGrainSize(ClasticGrainSize* oq);

  CarbonateGrainSize* createCarbonateGrainSize(int order,
					       const QString& name,
					       const QString& description,
					       GraphicColumnHeader::WidthPositions pos);
  void deleteCarbonateGrainSize(CarbonateGrainSize* oq);

  LengthUnit* createLengthUnit(int mm, const QString& name);

 private:
  QString _path;

  QList<Profile*> _profiles;
  QList<OutcropQuality*> _outcropQualities;
  QList<Color*> _colors;
  QList<Lithology*> _lithologies;
  QList<BeddingType*> _beddingTypes;
  QList<BoundaryType*> _boundaryTypes;
  QList<ClasticGrainSize*> _clasticGrainSizes;
  QList<CarbonateGrainSize*> _carbonateGrainSizes;
  QList<Fossil*> _fossils;
  QList<SedimentStructure*> _sedimentStructures;
  QList<CustomSymbol*> _customSymbols;
  QList<LengthUnit*> _lengthUnits;
  QList<Facies*> _facies;
  QList<LithologicalUnitType*> _lithologicalUnitTypes;
  QList<LithologicalUnit*> _lithologicalUnits;
  QList<ProfileCorrelation*> _profileCorrelations;

  int _lastProfileId;
  int _lastOutcropQualityId;
  int _lastColorId;
  int _lastLithologyId;
  int _lastBeddingTypeId;
  int _lastBoundaryTypeId;
  int _lastCarbonateGrainSizeId;
  int _lastClasticGrainSizeId;
  int _lastFossilId;
  int _lastSedimentStructureId;
  int _lastCustomSymbolId;
  int _lastLengthUnitId;
  int _lastFaciesId;
  int _lastLithologicalUnitTypeId;
  int _lastLithologicalUnitId;
  int _lastProfileCorrelationId;
};

#endif	/* _PROJECT_H */

