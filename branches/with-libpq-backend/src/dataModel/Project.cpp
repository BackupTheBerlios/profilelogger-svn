/* 
 * File:   Project.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 19:39
 */

#include "Project.h"

#include "Profile.h"
#include "ProfileCorrelation.h"
#include "OutcropQuality.h"
#include "Color.h"
#include "Lithology.h"
#include "BeddingType.h"
#include "BoundaryType.h"
#include "CarbonateGrainSize.h"
#include "ClasticGrainSize.h"
#include "Fossil.h"
#include "SedimentStructure.h"
#include "CustomSymbol.h"
#include "LengthUnit.h"
#include "GraphicColumnWidget.h"
#include "Facies.h"
#include "LithologicalUnitType.h"
#include "LithologicalUnit.h"
#include "LithologicalUnitTypeEditorDialog.h"

Project::Project(const int id,
		 const QString& name,
		 const QString& description,
		 const QString& path,
		 const bool isInDatabase)
  : Dataset(id,
	    name,
	    description,
	    isInDatabase),
    _path(path) {
  setupGrainSizes();
  setupLengthUnits();
    }

Project::~Project() {
  _profiles.clear();
  _outcropQualities.clear();
  _colors.clear();
  _lithologies.clear();
  _beddingTypes.clear();
  _boundaryTypes.clear();
  _carbonateGrainSizes.clear();
  _clasticGrainSizes.clear();
  _fossils.clear();
  _sedimentStructures.clear();
  _customSymbols.clear();
  _lengthUnits.clear();
  _facies.clear();
  _lithologicalUnitTypes.clear();
  _lithologicalUnits.clear();
  _profileCorrelations.clear();
}

Profile* Project::createProfile() {
  _profiles.append(new Profile(this, 
			       0,
			       QObject::tr("New Profile")));
  return getProfile(_lastProfileId);
}

Profile* Project::duplicateProfile(Profile* srcP) {
  Profile* p = createProfile();
  p->copyData(srcP);
  return p;
}

Profile* Project::getProfile(int id) {
  for (int i = 0; i < _profiles.size(); i++) {
    Profile* p = _profiles.at(i);

    if (p->getId() == id) {
      return p;
    }
  }
  return 0;
}

void Project::deleteProfile(Profile* p) {
  int i = _profiles.indexOf(p);

  if (-1 == i) {
    return;
  }

  Profile* pr = _profiles.takeAt(i);

  if (pr) {
    delete pr;
  }
}

OutcropQuality* Project::createOutcropQuality() {
  _outcropQualities.append(new OutcropQuality(this,
					      0, 
					      QObject::tr("New Outcrop Quality")));
  return _outcropQualities.last();
}

OutcropQuality* Project::getOutcropQuality(int id) {
  for (int i = 0; i < _outcropQualities.size(); i++) {
    OutcropQuality* oq = _outcropQualities.at(i);

    if (oq->getId() == id) {
      return oq;
    }
  }

  return 0;
}

void Project::deleteOutcropQuality(OutcropQuality* p) {
  int i = _outcropQualities.indexOf(p);

  if (-1 == i) {
    return;
  }

  OutcropQuality* q = _outcropQualities.takeAt(i);

  if (q) {
    delete q;
  }
}

Color* Project::createColor() {
  _colors.append(new Color(0, QObject::tr("New Color")));
  return _colors.last();
}

Color* Project::getColor(int id) {
  for (int i = 0; i < _colors.size(); i++) {
    Color* c = _colors.at(i);
    if (c->getId() == id) {
      return c;
    }
  }
  return 0;
}

void Project::deleteColor(Color* p) {
  int i = _colors.indexOf(p);

  if (-1 == i) {
    return;
  }

  Color* c = _colors.takeAt(i);

  if (c) {
    delete c;
  }
}

LithologicalUnitType* Project::createLithologicalUnitType() {
  _lithologicalUnitTypes.append(new LithologicalUnitType(0, QObject::tr("New Lithological Unit Type")));
  return _lithologicalUnitTypes.last();
}

LithologicalUnitType* Project::getLithologicalUnitType(int id) {
  for (int i = 0; i < _lithologicalUnitTypes.size(); i++) {
    LithologicalUnitType* t = _lithologicalUnitTypes.at(i);
    if (t->getId() == id) {
      return t;
    }
  }

  return 0;
}

void Project::deleteLithologicalUnitType(LithologicalUnitType* p) {
  int i = _lithologicalUnitTypes.indexOf(p);

  if (i == -1) {
    return;
  }

  LithologicalUnitType* t = _lithologicalUnitTypes.takeAt(i);

  if (t) {
    delete t;
  }
}

LithologicalUnit* Project::createLithologicalUnit() {
  _lithologicalUnits.append(new LithologicalUnit(0, 
						 QObject::tr("New Lithological Unit")));
  return _lithologicalUnits.last();
}

LithologicalUnit* Project::getLithologicalUnit(int id) {
  for (int i = 0; i < _lithologicalUnits.size(); i++) {
    LithologicalUnit* ret = _lithologicalUnits.at(i);
    if (id == ret->getId()) {
      return ret;
    }
  }

  return 0;
}

void Project::deleteLithologicalUnit(LithologicalUnit* p) {
  int i = _lithologicalUnits.indexOf(p);

  if (i == -1) {
    return;
  }

  LithologicalUnit* cand = _lithologicalUnits.takeAt(i);

  if (cand) {
    delete cand;
  }
}

Lithology* Project::createLithology() {
  _lithologies.append(new Lithology(this, 
				    _lastLithologyId, 
				    QObject::tr("New Lithology")));
  return _lithologies.last();
}

Lithology* Project::getLithology(int id) {
  for (int i = 0; i < _lithologies.size(); i++) {
    Lithology* l = _lithologies.at(i);

    if (l->getId() == id) {
      return l;
    }
  }

  return 0;
}

void Project::deleteLithology(Lithology* p) {
  int i = _lithologies.indexOf(p);

  if (-1 == i) {
    return;
  }

  Lithology* l = _lithologies.takeAt(i);

  if (l) {
    delete l;
  }
}

BeddingType* Project::createBeddingType() {
  _beddingTypes.append(new BeddingType(this,
				       0, 
				       QObject::tr("New BeddingType")));
  return _beddingTypes.last();
}

BeddingType* Project::getBeddingType(int id) {
  for (int i = 0; i < _beddingTypes.size(); i++) {
    BeddingType* t = _beddingTypes.at(i);

    if (t->getId() == id) {
      return t;
    }
  }

  return 0;
}

void Project::deleteBeddingType(BeddingType* p) {
  int i = _beddingTypes.indexOf(p);

  if (-1 == i) {
    return;
  }

  BeddingType* t = _beddingTypes.takeAt(i);

  if (t) {
    delete t;
  }
}

Facies* Project::createFacies() {
  _facies.append(new Facies(this,
			    0, 
			    QObject::tr("New Facies")));
  return _facies.last();
}

Facies* Project::getFacies(int id) {
  for (int i = 0; i < _facies.size(); i++) {
    Facies* f = _facies.at(i);

    if (f->getId() == id) {
      return f;
    }
  }

  return 0;
}

void Project::deleteFacies(Facies* p) {
  int i = _facies.indexOf(p);

  if (-1 == i) {
    return;
  }

  Facies* f = _facies.takeAt(i);

  if (f) {
    delete f;
  }
}

BoundaryType* Project::createBoundaryType() {
  _boundaryTypes.append(new BoundaryType(this,
					 0, 
					 QObject::tr("New BoundaryType")));
  return _boundaryTypes.last();
}

BoundaryType* Project::getBoundaryType(int id) {
  for (int i = 0; i < _boundaryTypes.size(); i++) {
    BoundaryType* t = _boundaryTypes.at(i);

    if (t->getId() == id) {
      return t;
    }
  }

  return 0;
}

void Project::deleteBoundaryType(BoundaryType* p) {
  int i = _boundaryTypes.indexOf(p);

  if (-1 == i) {
    return;
  }

  BoundaryType* t = _boundaryTypes.takeAt(i);

  if (t) {
    delete t;
  }
}

CarbonateGrainSize* Project::createCarbonateGrainSize(int order,
						      const QString& name,
						      const QString& description,
						      GraphicColumnHeader::WidthPositions pos) {
  _carbonateGrainSizes.append(new CarbonateGrainSize(0, 
						     order, 
						     name, 
						     description, 
						     pos));
  return _carbonateGrainSizes.last();
}

CarbonateGrainSize* Project::getCarbonateGrainSize(int id) {
  for (int i = 0; i < _carbonateGrainSizes.size(); i++) {
    CarbonateGrainSize* s = _carbonateGrainSizes.at(i);

    if (s->getId() == id) {
      return s;
    }

    return s;
  }

  return 0;
}

void Project::deleteCarbonateGrainSize(CarbonateGrainSize* p) {
  int i = _carbonateGrainSizes.indexOf(p);

  if (-1 == i) {
    return;
  }

  CarbonateGrainSize* s = _carbonateGrainSizes.takeAt(i);

  if (s) {
    delete s;
  }
}

ClasticGrainSize* Project::createClasticGrainSize(int order,
						  const QString& name,
						  const QString& description,
						  GraphicColumnHeader::WidthPositions pos) {
  _clasticGrainSizes.append(new ClasticGrainSize(0, order, name, description, pos));
  return _clasticGrainSizes.last();
}

ClasticGrainSize* Project::getClasticGrainSize(int id) {
  for (int i = 0; i < _clasticGrainSizes.size(); i++) {
    ClasticGrainSize* s = _clasticGrainSizes.at(i);
    if (s->getId() == id) {
      return s;
    }
  }

  return 0;
}

void Project::deleteClasticGrainSize(ClasticGrainSize* p) {
  if (!p) {
    return;
  }

  int i = _clasticGrainSizes.indexOf(p);

  if (-1 == i) {
    return;
  }

  ClasticGrainSize* s = _clasticGrainSizes.takeAt(i);

  if (s) {
    delete s;
  }
}

void Project::setupGrainSizes() {
  setupClasticGrainSizes();
  setupCarbonateGrainSizes();
}

void Project::setupLengthUnits() {
  (void) createLengthUnit(1, "mm");
  (void) createLengthUnit(10, "cm");
  (void) createLengthUnit(100, "dm");
  (void) createLengthUnit(1000, "m");
  (void) createLengthUnit(1000000, "km");
}

void Project::setupClasticGrainSizes() {
  int o = 1;
  (void) createClasticGrainSize(o++, QObject::tr("No Grains Visible"), QString::null, GraphicColumnHeader::NoClasticGrainsEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Clay"), QString::null, GraphicColumnHeader::ClayEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Fine Silt"), QString::null, GraphicColumnHeader::FineSiltEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Medium Silt"), QString::null, GraphicColumnHeader::MediumSiltEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Coarse Silt"), QString::null, GraphicColumnHeader::CoarseSiltEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Fine Sand"), QString::null, GraphicColumnHeader::FineSandEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Medium Sand"), QString::null, GraphicColumnHeader::SandEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Coarse Sand"), QString::null, GraphicColumnHeader::CoarseSandEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Fine Gravel"), QString::null, GraphicColumnHeader::FineGravelEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Medium Gravel"), QString::null, GraphicColumnHeader::GravelEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Coarse Gravel"), QString::null, GraphicColumnHeader::CoarseGravelEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Cobbles"), QString::null, GraphicColumnHeader::CobblesEnd);
  (void) createClasticGrainSize(o++, QObject::tr("Blocks"), QString::null, GraphicColumnHeader::BlocksEnd);
}

void Project::setupCarbonateGrainSizes() {
  int o = 1;
  (void) createCarbonateGrainSize(o++, QObject::tr("Evaporite"), QString::null, GraphicColumnHeader::EvaporiteEnd);
  (void) createCarbonateGrainSize(o++, QObject::tr("Mudstone"), QString::null, GraphicColumnHeader::MudstoneEnd);
  (void) createCarbonateGrainSize(o++, QObject::tr("Wackestone"), QString::null, GraphicColumnHeader::WackestoneEnd);
  (void) createCarbonateGrainSize(o++, QObject::tr("Packstone"), QString::null, GraphicColumnHeader::PackstoneEnd);
  (void) createCarbonateGrainSize(o++, QObject::tr("Grainstone"), QString::null, GraphicColumnHeader::GrainstoneEnd);
  (void) createCarbonateGrainSize(o++, QObject::tr("Rudstone"), QString::null, GraphicColumnHeader::RudstoneEnd);
}

Fossil* Project::createFossil() {
  _fossils.append(new Fossil(this,
			     0, 
			     QObject::tr("New Fossil")));
  return _fossils.last();
}

Fossil* Project::getFossil(int id) {
  for (int i = 0; i < _fossils.size(); i++) {
    Fossil* f = _fossils.at(i);

    if (f->getId() == id) {
      return f;
    }
  }

  return 0;
}

void Project::deleteFossil(Fossil* p) {
  if (!p) {
    return;
  }

  int i = _fossils.indexOf(p);

  if (-1 == i) {
    return;
  }

  Fossil* f = _fossils.takeAt(i);

  if (f) {
    delete f;
  }
}

SedimentStructure* Project::createSedimentStructure() {
  _sedimentStructures.append(new SedimentStructure(this,
						   0, 
						   QObject::tr("New SedimentStructure")));
  return _sedimentStructures.last();
}

SedimentStructure* Project::getSedimentStructure(int id) {
  for (int i = 0; i < _sedimentStructures.size(); i++) {
    SedimentStructure* s = _sedimentStructures.at(i);

    if (s->getId() == id) {
      return s;
    }
  }

  return 0;
}

void Project::deleteSedimentStructure(SedimentStructure* p) {
  if (!p) {
    return;
  }

  int i = _sedimentStructures.indexOf(p);

  SedimentStructure* s = _sedimentStructures.takeAt(i);

  if (s) {
    delete s;
  }
}

CustomSymbol* Project::createCustomSymbol() {
  _customSymbols.append(new CustomSymbol(this,
					 0, 
					 QObject::tr("New CustomSymbol")));
  return _customSymbols.last();
}

CustomSymbol* Project::getCustomSymbol(int id) {
  for(int i = 0; i < _customSymbols.size(); i++) {
    CustomSymbol* s = _customSymbols.at(i);

    if (s->getId() == id) {
      return s;
    }
  }

  return 0;
}

void Project::deleteCustomSymbol(CustomSymbol* p) {
  if (!p) {
    return;
  }

  int i = _customSymbols.indexOf(p);

  if (-1 == i) {
    return;
  }

  CustomSymbol* s = _customSymbols.takeAt(i);

  if (s) {
    delete s;
  }
}

LengthUnit* Project::createLengthUnit(int mm, const QString& name) {
  _lengthUnits.append(new LengthUnit(0, mm, name));
  return _lengthUnits.last();
}

LengthUnit* Project::getLengthUnit(int id) {
  for(int i = 0; i < _lengthUnits.size(); i++) {
    LengthUnit* u = _lengthUnits.at(i);

    if (u->getId() == id) {
      return u;
    }
  }

  return 0;
}

LengthUnit* Project::getDefaultLengthUnit() {
  if (_lengthUnits.size() < 1) {
    return 0;
  }
  return _lengthUnits.at(0);
}

ProfileCorrelation* Project::createProfileCorrelation() {
  _profileCorrelations.append(new ProfileCorrelation(0, 
						     QObject::tr("New ProfileCorrelation")));
  return _profileCorrelations.last();
}

ProfileCorrelation* Project::duplicateProfileCorrelation(ProfileCorrelation* srcP) {
  ProfileCorrelation* p = createProfileCorrelation();
  p->copyData(srcP);
  return p;
}

ProfileCorrelation* Project::getProfileCorrelation(int id) {
  for (int i = 0; i < _profileCorrelations.size(); i++) {
    ProfileCorrelation* p = _profileCorrelations.at(i);

    if (p->getId() == id) {
      return p;
    }
  }
  return 0;
}

void Project::deleteProfileCorrelation(ProfileCorrelation* p) {
  int i = _profileCorrelations.indexOf(p);

  if (-1 == i) {
    return;
  }

  ProfileCorrelation* pr = _profileCorrelations.takeAt(i);

  if (pr) {
    delete pr;
  }
}
