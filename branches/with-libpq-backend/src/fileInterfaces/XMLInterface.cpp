/* 
 * File:   XMLInterface.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 19:50
 */

#include <QApplication>
#include <QMessageBox>
#include <QFileDialog>
#include <QVariant>
#include <QTextStream>
#include <QDebug>

#include "MainWindow.h"
#include "XMLInterface.h"
#include "Project.h"
#include "ProfileLogger.h"
#include "Profile.h"
#include "ProfileCorrelation.h"
#include "Bed.h"
#include "BedCorrelation.h"
#include "OutcropQuality.h"
#include "Color.h"
#include "Lithology.h"
#include "BeddingType.h"
#include "BoundaryType.h"
#include "GrainSizeModes.h"
#include "ClasticGrainSize.h"
#include "CarbonateGrainSize.h"
#include "GrainSizeModes.h"
#include "Fossil.h"
#include "SedimentStructure.h"
#include "CustomSymbol.h"
#include "LengthUnit.h"
#include "LengthMeasurement.h"
#include "Facies.h"
#include "LithologicalUnitType.h"
#include "LithologicalUnit.h"
#include "Sample.h"
#include "Image.h"
#include "Version.h"

XMLInterface::XMLInterface(QObject* p)
  : QObject(p),
    _project(0) {
}

XMLInterface::~XMLInterface() {
}

void XMLInterface::saveOutcropQualities() {
  _outcropQualitiesE = _doc.createElement("OutcropQualities");
  for (QList<OutcropQuality*>::iterator it = _project->getFirstOutcropQuality();
       it != _project->getLastOutcropQuality();
       it++) {
    OutcropQuality* q = *it;
    QDomElement e = _doc.createElement("OutcropQuality");
    e.setAttribute("id", q->getId());
    e.setAttribute("name", q->getName());
    e.setAttribute("description", q->getDescription());
    e.setAttribute("patternFileName", q->getFileName());
    _outcropQualitiesE.appendChild(e);
  }
  _metaE.appendChild(_outcropQualitiesE);
}

void XMLInterface::saveColors() {
  _colorsE = _doc.createElement("Colors");
  for (QList<Color*>::iterator it = _project->getFirstColor();
       it != _project->getLastColor();
       it++) {
    Color* c = *it;
    QDomElement e = _doc.createElement("Color");
    e.setAttribute("id", c->getId());
    e.setAttribute("name", c->getName());
    e.setAttribute("description", c->getDescription());
    e.setAttribute("QtBrushStyle", (int) c->getBrushStyle());
    _colorsE.appendChild(e);
  }
  _metaE.appendChild(_colorsE);
}

void XMLInterface::saveLithologicalUnits() {
  _lithologicalUnitsE = _doc.createElement("LithologicalUnits");
  for (QList<LithologicalUnit*>::iterator it = _project->getFirstLithologicalUnit();
       it != _project->getLastLithologicalUnit();
       it++) {
    LithologicalUnit* u = *it;
    QDomElement e = _doc.createElement("LithologicalUnit");
    e.setAttribute("id", u->getId());
    e.setAttribute("name", u->getName());
    e.setAttribute("description", u->getDescription());
    if ((*it)->hasLithologicalUnitType()) {
      e.setAttribute("lithologicalUnitTypeId", u->getLithologicalUnitType()->getId());
    }
    _lithologicalUnitsE.appendChild(e);
  }
  _metaE.appendChild(_lithologicalUnitsE);
}

void XMLInterface::saveLithologicalUnitTypes() {
  _lithologicalUnitTypesE = _doc.createElement("LithologicalUnitTypes");
  for (QList<LithologicalUnitType*>::iterator it = _project->getFirstLithologicalUnitType();
       it != _project->getLastLithologicalUnitType();
       it++) {
    LithologicalUnitType* u = *it;
    QDomElement e = _doc.createElement("LithologicalUnitType");
    e.setAttribute("id", u->getId());
    e.setAttribute("name", u->getName());
    e.setAttribute("description", u->getDescription());
    _lithologicalUnitTypesE.appendChild(e);
  }
  _metaE.appendChild(_lithologicalUnitTypesE);
}

void XMLInterface::saveFacies() {
  _faciesE = _doc.createElement("Facies");
  for (QList<Facies*>::iterator it = _project->getFirstFacies();
       it != _project->getLastFacies();
       it++) {
    Facies* f = *it;
    QDomElement e = _doc.createElement("Facies");
    e.setAttribute("id", f->getId());
    e.setAttribute("name", f->getName());
    e.setAttribute("description", f->getDescription());
    e.setAttribute("patternFileName", f->getFileName());
    _faciesE.appendChild(e);
  }
  _metaE.appendChild(_faciesE);
}

void XMLInterface::saveLithologies() {
  _lithologiesE = _doc.createElement("Lithologies");
  for (QList<Lithology*>::iterator it = _project->getFirstLithology();
       it != _project->getLastLithology();
       it++) {
    Lithology* l = *it;
    QDomElement e = _doc.createElement("Lithology");
    e.setAttribute("id", l->getId());
    e.setAttribute("name", l->getName());
    e.setAttribute("description", l->getDescription());
    e.setAttribute("patternFileName", l->getFileName());
    e.setAttribute("defaultGrainSizeMode", (int) l->getDefaultGrainSizeMode());
    if (l->hasDefaultCarbonateGrainSize()) {
      e.setAttribute("defaultCarbonateGrainSizeId", l->getDefaultCarbonateGrainSize()->getId());
    }
    if (l->hasDefaultClasticGrainSize()) {
      e.setAttribute("defaultClasticGrainSizeId", l->getDefaultClasticGrainSize()->getId());
    }
    _lithologiesE.appendChild(e);
  }
  _metaE.appendChild(_lithologiesE);
}

void XMLInterface::saveLengthUnits() {
  _lengthUnitsE = _doc.createElement("LengthUnits");
  for (QList<LengthUnit*>::iterator it = _project->getFirstLengthUnit();
       it != _project->getLastLengthUnit();
       it++) {
    LengthUnit* u = *it;
    QDomElement e = _doc.createElement("LengthUnit");
    e.setAttribute("id", u->getId());
    e.setAttribute("name", u->getName());
    e.setAttribute("description", u->getDescription());
    e.setAttribute("mm", u->getMilliMetre());
    _lengthUnitsE.appendChild(e);
  }
  _metaE.appendChild(_lengthUnitsE);
}

void XMLInterface::saveClasticGrainSizes() {
  _clasticGrainSizesE = _doc.createElement("ClasticGrainSizes");
  for (QList<ClasticGrainSize*>::iterator it = _project->getFirstClasticGrainSize();
       it != _project->getLastClasticGrainSize();
       it++) {
    ClasticGrainSize* s = *it;
    QDomElement e = _doc.createElement("ClasticGrainSize");
    e.setAttribute("id", s->getId());
    e.setAttribute("name", s->getName());
    e.setAttribute("description", s->getDescription());
    e.setAttribute("positionInColumnView", (int) (s->getPosition()));
    _clasticGrainSizesE.appendChild(e);
  }
  _metaE.appendChild(_clasticGrainSizesE);
}

void XMLInterface::saveCarbonateGrainSizes() {
  _carbonateGrainSizesE = _doc.createElement("CarbonateGrainSizes");
  for (QList<CarbonateGrainSize*>::iterator it = _project->getFirstCarbonateGrainSize();
       it != _project->getLastCarbonateGrainSize();
       it++) {
    CarbonateGrainSize* s = *it;
    QDomElement e = _doc.createElement("CarbonateGrainSize");
    e.setAttribute("id", s->getId());
    e.setAttribute("name", s->getName());
    e.setAttribute("description", s->getDescription());
    e.setAttribute("positionInColumnView", (int) (s->getPosition()));
    _carbonateGrainSizesE.appendChild(e);
  }
  _metaE.appendChild(_carbonateGrainSizesE);
}

void XMLInterface::saveBeddingTypes() {
  _beddingTypesE = _doc.createElement("BeddingTypes");
  for (QList<BeddingType*>::iterator it = _project->getFirstBeddingType();
       it != _project->getLastBeddingType();
       it++) {
    BeddingType* t = *it;
    QDomElement e = _doc.createElement("BeddingType");
    e.setAttribute("id", t->getId());
    e.setAttribute("name", t->getName());
    e.setAttribute("description", t->getDescription());
    e.setAttribute("patternFileName", t->getFileName());
    _beddingTypesE.appendChild(e);
  }
  _metaE.appendChild(_beddingTypesE);
}

void XMLInterface::saveBoundaryTypes() {
  _boundaryTypesE = _doc.createElement("BoundaryTypes");
  for (QList<BoundaryType*>::iterator it = _project->getFirstBoundaryType();
       it != _project->getLastBoundaryType();
       it++) {
    BoundaryType* t = *it;
    QDomElement e = _doc.createElement("BoundaryType");
    e.setAttribute("id", t->getId());
    e.setAttribute("name", t->getName());
    e.setAttribute("description", t->getDescription());
    e.setAttribute("fileName", t->getFileName());
    _boundaryTypesE.appendChild(e);
  }
  _metaE.appendChild(_boundaryTypesE);
}

void XMLInterface::saveFossils() {
  _fossilsE = _doc.createElement("Fossils");
  for (QList<Fossil*>::iterator it = _project->getFirstFossil();
       it != _project->getLastFossil();
       it++) {
    Fossil* f = *it;
    QDomElement e = _doc.createElement("Fossil");
    e.setAttribute("id", f->getId());
    e.setAttribute("name", f->getName());
    e.setAttribute("description", f->getDescription());
    e.setAttribute("pictureFileName", f->getFileName());
    _fossilsE.appendChild(e);
  }
  _metaE.appendChild(_fossilsE);
}

void XMLInterface::saveSedimentStructures() {
  _sedimentStructuresE = _doc.createElement("SedimentStructures");
  for (QList<SedimentStructure*>::iterator it = _project->getFirstSedimentStructure();
       it != _project->getLastSedimentStructure();
       it++) {
    SedimentStructure* s = *it;
    QDomElement e = _doc.createElement("SedimentStructure");
    e.setAttribute("id", s->getId());
    e.setAttribute("name", s->getName());
    e.setAttribute("description", s->getDescription());
    e.setAttribute("pictureFileName", s->getFileName());

    _sedimentStructuresE.appendChild(e);
  }
  _metaE.appendChild(_sedimentStructuresE);
}

void XMLInterface::saveCustomSymbols() {
  _customSymbolsE = _doc.createElement("CustomSymbols");
  for (QList<CustomSymbol*>::iterator it = _project->getFirstCustomSymbol();
       it != _project->getLastCustomSymbol();
       it++) {
    CustomSymbol* s = *it;
    QDomElement e = _doc.createElement("CustomSymbol");
    e.setAttribute("id", s->getId());
    e.setAttribute("name", s->getName());
    e.setAttribute("description", s->getDescription());
    e.setAttribute("pictureFileName", s->getFileName());

    _customSymbolsE.appendChild(e);
  }
  _metaE.appendChild(_customSymbolsE);
}

void XMLInterface::saveProfileCorrelations() {
  QDomElement ge = _doc.createElement("ProfileCorrelations");

  for (QList<ProfileCorrelation*>::iterator it = _project->getFirstProfileCorrelation();
       it != _project->getLastProfileCorrelation();
       it++) {
    QDomElement e = _doc.createElement("ProfileCorrelation");
    ProfileCorrelation* c = *it;
    e.setAttribute("id", c->getId());
    e.setAttribute("name", c->getName());
    e.setAttribute("description", c->getDescription());
    
    for (QList<BedCorrelation*>::iterator bit = c->getFirstBedCorrelation();
	 bit != c->getLastBedCorrelation();
	 bit++) {
      BedCorrelation* bedCorr = *bit;
      saveBedCorrelation(bedCorr, e);
    }

    ge.appendChild(e);
  }

  _dataE.appendChild(ge);
}

void XMLInterface::saveBedCorrelation(BedCorrelation* c, QDomElement& groupE) {
  if (!c) {
    return;
  }

  QDomElement e = _doc.createElement("BedCorrelation");

  if (c->hasLeftBed()) {
    Bed* left = c->getLeftBed();
    if (left->hasProfile()) {
      e.setAttribute("leftProfileId", left->getProfile()->getId());
      e.setAttribute("leftBedId", left->getId());
    }
  }

  if (c->hasRightBed()) {
    Bed* right = c->getRightBed();
    if (right->hasProfile()) {
      e.setAttribute("rightProfileId", right->getProfile()->getId());
      e.setAttribute("rightBedId", right->getId());
    }
  }

  groupE.appendChild(e);
}

void XMLInterface::saveProfiles() {
  _dataE = _doc.createElement("Data");

  for (QList<Profile*>::iterator it = _project->getFirstProfile();
       it != _project->getLastProfile();
       it++) {
    saveProfile(*it);
  }

  _doc.documentElement().appendChild(_dataE);
}

void XMLInterface::saveProfile(Profile* profile) {
  QDomElement profileE = _doc.createElement("Profile");

  profileE.setAttribute("id", profile->getId());
  profileE.setAttribute("name", profile->getName());
  profileE.setAttribute("description", profile->getDescription());
  profileE.setAttribute("maxSymbolSize", profile->getMaxSymbolSize());
  profileE.setAttribute("scale", profile->getScale());
  profileE.setAttribute("cellSize", profile->getCellSize());
  profileE.setAttribute("bigMarksDistanceValue", profile->getBigMarksDistance()->getValue());
  profileE.setAttribute("bigMarksDistanceLengthUnitId", profile->getBigMarksDistance()->getUnit()->getId());
  profileE.setAttribute("smallMarksDistanceValue", profile->getSmallMarksDistance()->getValue());
  profileE.setAttribute("smallMarksDistanceLengthUnitId", profile->getSmallMarksDistance()->getUnit()->getId());
  profileE.setAttribute("legendColumns", profile->getLegendColumns());
  profileE.setAttribute("showHeight", (int)profile->getShowHeight());
  profileE.setAttribute("showBedNumbers", (int)profile->getShowBedNumbers());
  profileE.setAttribute("showLithology", (int)profile->getShowLithology());
  profileE.setAttribute("showBeddingType", (int)profile->getShowBeddingType());
  profileE.setAttribute("showTopBoundaryType", (int)profile->getShowTopBoundaryType());
  profileE.setAttribute("showFossils", (int)profile->getShowFossils());
  profileE.setAttribute("showSedimentStructures", (int)profile->getShowSedimentStructures());
  profileE.setAttribute("showGrainSize", (int)profile->getShowGrainSize());
  profileE.setAttribute("showCustomSymbols", (int)profile->getShowCustomSymbols());
  profileE.setAttribute("showNotes", (int)profile->getShowNotes());
  profileE.setAttribute("showColor", (int)profile->getShowColor());
  profileE.setAttribute("showFacies", (int)profile->getShowFacies());
  profileE.setAttribute("showLithologicalUnit", (int)profile->getShowLithologicalUnit());
  profileE.setAttribute("showOutcropQuality", (int)profile->getShowOutcropQuality());
  profileE.setAttribute("showHeightMarks", (int)profile->getShowHeightMarks());

  if (profile->hasDefaultUnit()) {
    profileE.setAttribute("defaultLengthUnitId", profile->getDefaultUnit()->getId());
  }

  QDomElement samplesE = _doc.createElement("Samples");
  for (QList<Sample*>::iterator it = profile->getFirstSample();
       it != profile->getLastSample();
       it++) {
    Sample* s = *it;
    QDomElement e = _doc.createElement("Sample");
    e.setAttribute("id", s->getId());
    e.setAttribute("name", s->getName());
    e.setAttribute("description", s->getDescription());
    samplesE.appendChild(e);

  }
  profileE.appendChild(samplesE);

  QDomElement imagesE = _doc.createElement("Images");
  for (QList<Image*>::iterator it = profile->getFirstImage();
       it != profile->getLastImage();
       it++) {
    Image* i = *it;
    QDomElement e = _doc.createElement("Image");
    e.setAttribute("id", i->getId());
    e.setAttribute("name", i->getName());
    e.setAttribute("description", i->getDescription());
    e.setAttribute("fileName", i->getFileName());
    imagesE.appendChild(e);
  }
  profileE.appendChild(imagesE);

  int bedCnt = profile->getBedCount();

  for (int bedIdx = 0; bedIdx < bedCnt; bedIdx++) {
    Bed* bed = profile->getBedByPosition(bedIdx);
    QDomElement bedE = _doc.createElement("Bed");
    saveBed(bed, bedE);
    profileE.appendChild(bedE);
  }

  _dataE.appendChild(profileE);
}

void XMLInterface::saveFossilsInBed(Bed* bed, QDomElement& bedE) {
  QDomElement fossilsInBedE = _doc.createElement("FossilsInBed");
  for (QList<Fossil*>::iterator it = bed->getFirstFossil(); it != bed->getLastFossil(); it++) {
    QDomElement tmpE = _doc.createElement("FossilInBed");
    if (*it) {
      tmpE.setAttribute("fossilId", (*it)->getId());
      tmpE.setAttribute("fossilName", (*it)->getName());
      fossilsInBedE.appendChild(tmpE);
    }
  }
  bedE.appendChild(fossilsInBedE);
}

void XMLInterface::saveSedimentStructuresInBed(Bed* bed, QDomElement& bedE) {
  QDomElement sedimentStructuresInBedE = _doc.createElement("SedimentStructuresInBed");
  for (QList<SedimentStructure*>::iterator it = bed->getFirstSedimentStructure(); it != bed->getLastSedimentStructure(); it++) {
    QDomElement tmpE = _doc.createElement("SedimentStructureInBed");
    if (*it) {
      tmpE.setAttribute("sedimentStructureId", (*it)->getId());
      tmpE.setAttribute("sedimentStructureName", (*it)->getName());
      sedimentStructuresInBedE.appendChild(tmpE);
    }
  }
  bedE.appendChild(sedimentStructuresInBedE);
}

void XMLInterface::saveCustomSymbolsInBed(Bed* bed, QDomElement& bedE) {
  QDomElement customSymbolsInBedE = _doc.createElement("CustomSymbolsInBed");
  for (QList<CustomSymbol*>::iterator it = bed->getFirstCustomSymbol(); it != bed->getLastCustomSymbol(); it++) {
    QDomElement tmpE = _doc.createElement("CustomSymbolInBed");
    if (*it) {
      tmpE.setAttribute("customSymbolId", (*it)->getId());
      tmpE.setAttribute("customSymbolName", (*it)->getName());
      customSymbolsInBedE.appendChild(tmpE);
    }
  }
  bedE.appendChild(customSymbolsInBedE);
}

void XMLInterface::saveBed(Bed* bed, QDomElement& bedE) {
  bedE.setAttribute("grainSizeMode", bed->getGrainSizeMode());
  bedE.setAttribute("id", bed->getId());
  bedE.setAttribute("position", bed->getPosition());
  bedE.setAttribute("description", bed->getDescription());

  LengthMeasurement* h = bed->getHeight();
  bedE.setAttribute("heightValue", h->getValue());
  if (h->hasUnit()) {
    bedE.setAttribute("heightLengthUnitId", h->getUnit()->getId());
  }

  if (bed->hasOutcropQuality()) {
    bedE.setAttribute("outcropQualityId", bed->getOutcropQuality()->getId());
  }
  if (bed->hasColor()) {
    bedE.setAttribute("colorId", bed->getColor()->getId());
  }
  if (bed->hasLithologicalUnit()) {
    bedE.setAttribute("lithologicalUnitId", bed->getLithologicalUnit()->getId());
  }
  if (bed->hasFacies()) {
    bedE.setAttribute("faciesId", bed->getFacies()->getId());
  }
  if (bed->hasLithology()) {
    bedE.setAttribute("lithologyId", bed->getLithology()->getId());
  }
  if (bed->hasBeddingType()) {
    bedE.setAttribute("beddingTypeId", bed->getBeddingType()->getId());
  }
  if (bed->hasTopBoundaryType()) {
    bedE.setAttribute("topBoundaryTypeId", bed->getTopBoundaryType()->getId());
  }

  bedE.setAttribute("grainSizeMode", (int) bed->getGrainSizeMode());

  if (bed->hasBaseCarbonateGrainSize()) {
    bedE.setAttribute("baseCarbonateGrainSizeId", bed->getBaseCarbonateGrainSize()->getId());
  }
  if (bed->hasTopCarbonateGrainSize()) {
    bedE.setAttribute("topCarbonateGrainSizeId", bed->getTopCarbonateGrainSize()->getId());
  }
  if (bed->hasBaseClasticGrainSize()) {
    bedE.setAttribute("baseClasticGrainSizeId", bed->getBaseClasticGrainSize()->getId());
  }
  if (bed->hasTopClasticGrainSize()) {
    bedE.setAttribute("topClasticGrainSizeId", bed->getTopClasticGrainSize()->getId());
  }

  saveFossilsInBed(bed, bedE);
  saveSedimentStructuresInBed(bed, bedE);
  saveCustomSymbolsInBed(bed, bedE);
}

void XMLInterface::saveMetadata() {
  saveOutcropQualities();
  saveColors();
  saveFacies();
  saveLithologies();
  saveLengthUnits();
  saveClasticGrainSizes();
  saveCarbonateGrainSizes();
  saveBeddingTypes();
  saveBoundaryTypes();
  saveFossils();
  saveSedimentStructures();
  saveCustomSymbols();
  saveLithologicalUnitTypes();
  saveLithologicalUnits();
}

bool XMLInterface::save(Project* p) {
  if (!p) {
    return false;
  }
  _project = p;

  if (_project->getPath().isEmpty()) {
    return getProjectPathFromUserAndSave();
  }

  QFile f(_project->getPath());
  if (!f.open(QIODevice::Truncate | QIODevice::WriteOnly)) {
    QMessageBox::critical((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
			  tr("Could Not Open File"),
			  tr("Could not write to file %1").arg(f.fileName()));
    return false;
  }

  _doc = QDomDocument("ProfileLogger");
  _doc.appendChild(_doc.createElement("ProfileLogger"));
  _metaE = _doc.createElement("Metadata");
  _metaE.setAttribute("ProgramVersion", version);
  _doc.documentElement().appendChild(_metaE);

  saveMetadata();
  saveProfiles();
  saveProfileCorrelations();

  QTextStream strm(&f);
  strm << _doc.toString(4);
  f.close();

  return true;
}

void XMLInterface::loadOutcropQualities() {
  /*  QDomNodeList outcropQualities = _metaE.elementsByTagName("OutcropQuality");
  for (int i = 0; i < outcropQualities.size(); i++) {
    QDomElement e = outcropQualities.at(i).toElement();
    OutcropQuality* ocq = _project->createOutcropQuality(e.attribute("id").toInt());
    ocq->setName(e.attribute("name"));
    ocq->setDescription(e.attribute("description"));
    ocq->setFileName(e.attribute("patternFileName"));
    }*/
}

void XMLInterface::loadFacies() {
  /*  QDomNodeList facies = _metaE.elementsByTagName("Facies");
  for (int i = 0; i < facies.size(); i++) {
    QDomElement e = facies.at(i).toElement();
    Facies* c = _project->createFacies(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    c->setFileName(e.attribute("patternFileName"));
    }*/
 }

void XMLInterface::loadColors() {
  /*  QDomNodeList colors = _metaE.elementsByTagName("Color");
  for (int i = 0; i < colors.size(); i++) {
    QDomElement e = colors.at(i).toElement();
    Color* c = _project->createColor(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    c->setBrushStyle((Qt::BrushStyle)e.attribute("QtBrushStyle").toInt());
    }*/
}

void XMLInterface::loadLithologicalUnitTypes() {
  /*  QDomNodeList lithologicalUnitTypes = _metaE.elementsByTagName("LithologicalUnitType");
  for (int i = 0; i < lithologicalUnitTypes.size(); i++) {
    QDomElement e = lithologicalUnitTypes.at(i).toElement();
    LithologicalUnitType* c = _project->createLithologicalUnitType(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    }*/
}

void XMLInterface::loadLithologicalUnits() {
  /*  QDomNodeList lithologicalUnits = _metaE.elementsByTagName("LithologicalUnit");
  for (int i = 0; i < lithologicalUnits.size(); i++) {
    QDomElement e = lithologicalUnits.at(i).toElement();
    LithologicalUnit* c = _project->createLithologicalUnit(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));

    if (e.hasAttribute("lithologicalUnitTypeId")) {
      c->setLithologicalUnitType(_project->getLithologicalUnitType(e.attribute("lithologicalUnitTypeId").toInt()));
    }
    }*/
}

void XMLInterface::loadLithologies() {
  /*  QDomNodeList lithologies = _metaE.elementsByTagName("Lithology");
  for (int i = 0; i < lithologies.size(); i++) {
    QDomElement e = lithologies.at(i).toElement();
    Lithology* c = _project->createLithology(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    c->setFileName(e.attribute("patternFileName"));

    if (e.hasAttribute("defaultGrainSizeMode")) {
      if (e.attribute("defaultGrainSizeMode").toInt() == ClasticGrainSizeMode) {
	c->setDefaultGrainSizeMode(ClasticGrainSizeMode);
      }
      if (e.attribute("defaultGrainSizeMode").toInt() == CarbonateGrainSizeMode) {
	c->setDefaultGrainSizeMode(CarbonateGrainSizeMode);
      }
    }

    if (e.hasAttribute("defaultCarbonateGrainSizeId")) {
      c->setDefaultCarbonateGrainSize(_project->getCarbonateGrainSize(e.attribute("defaultCarbonateGrainSizeId").toInt()));
    }
    if (e.hasAttribute("defaultClasticGrainSizeId")) {
      c->setDefaultClasticGrainSize(_project->getClasticGrainSize(e.attribute("defaultClasticGrainSizeId").toInt()));
    }
    }*/
}

void XMLInterface::loadBeddingTypes() {
  /*  QDomNodeList beddingTypes = _metaE.elementsByTagName("BeddingType");
  for (int i = 0; i < beddingTypes.size(); i++) {
    QDomElement e = beddingTypes.at(i).toElement();
    BeddingType* c = _project->createBeddingType(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    c->setFileName(e.attribute("patternFileName"));
    }*/
}

void XMLInterface::loadBoundaryTypes() {
  /*  QDomNodeList boundaryTypes = _metaE.elementsByTagName("BoundaryType");
  for (int i = 0; i < boundaryTypes.size(); i++) {
    QDomElement e = boundaryTypes.at(i).toElement();
    BoundaryType* c = _project->createBoundaryType(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    c->setFileName(e.attribute("fileName"));
    }*/
}

void XMLInterface::loadFossils() {
  /*  QDomNodeList fossils = _metaE.elementsByTagName("Fossil");
  for (int i = 0; i < fossils.size(); i++) {
    QDomElement e = fossils.at(i).toElement();
    Fossil* c = _project->createFossil(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    c->setFileName(e.attribute("pictureFileName"));
    }*/
}

void XMLInterface::loadSedimentStructures() {
  /*  QDomNodeList sedimentStructures = _metaE.elementsByTagName("SedimentStructure");
  for (int i = 0; i < sedimentStructures.size(); i++) {
    QDomElement e = sedimentStructures.at(i).toElement();
    SedimentStructure* c = _project->createSedimentStructure(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    c->setFileName(e.attribute("pictureFileName"));
    }*/
}

void XMLInterface::loadCustomSymbols() {
  /*  QDomNodeList customSymbols = _metaE.elementsByTagName("CustomSymbol");
  for (int i = 0; i < customSymbols.size(); i++) {
    QDomElement e = customSymbols.at(i).toElement();
    CustomSymbol* c = _project->createCustomSymbol(e.attribute("id").toInt());
    c->setName(e.attribute("name"));
    c->setDescription(e.attribute("description"));
    c->setFileName(e.attribute("pictureFileName"));
    }*/
}

void XMLInterface::loadMetadata() {
  /*  QDomNodeList lMeta = _doc.documentElement().elementsByTagName("Metadata");

  if (lMeta.size() == 1) {
    _metaE = lMeta.at(0).toElement();
    loadOutcropQualities();
    loadColors();
    loadFacies();
    loadLithologies();
    loadBeddingTypes();
    loadBoundaryTypes();
    loadFossils();
    loadSedimentStructures();
    loadCustomSymbols();
    loadLithologicalUnitTypes();
    loadLithologicalUnits();
    }*/
}

void XMLInterface::loadFossilsInBed(Bed* bed, QDomElement& bedE) {
  (void) bed;
  (void) bedE;
  /*  QDomElement fossilsInBedE = bedE.elementsByTagName("FossilsInBed").item(0).toElement();

  QDomNodeList fossilsInBedNodes = fossilsInBedE.elementsByTagName("FossilInBed");

  for (int n = 0; n != fossilsInBedNodes.size(); n++) {
    QDomElement e = fossilsInBedNodes.item(n).toElement();
    bed->addFossil(_project->getFossil(e.attribute("fossilId").toInt()));
    }*/
}

void XMLInterface::loadSedimentStructuresInBed(Bed* bed, QDomElement& bedE) {
  (void) bed;
  (void) bedE;
  /*  QDomElement SedimentStructuresInBedE = bedE.elementsByTagName("SedimentStructuresInBed").item(0).toElement();

  QDomNodeList sedimentStructuresInBedNodes = SedimentStructuresInBedE.elementsByTagName("SedimentStructureInBed");

  for (int n = 0; n != sedimentStructuresInBedNodes.size(); n++) {
    QDomElement e = sedimentStructuresInBedNodes.item(n).toElement();
    bed->addSedimentStructure(_project->getSedimentStructure(e.attribute("sedimentStructureId").toInt()));
    }*/
}

void XMLInterface::loadCustomSymbolsInBed(Bed* bed, QDomElement& bedE) {
  (void) bed;
  (void) bedE;
  /*  QDomElement CustomSymbolsInBedE = bedE.elementsByTagName("CustomSymbolsInBed").item(0).toElement();

  QDomNodeList customSymbolsInBedNodes = CustomSymbolsInBedE.elementsByTagName("CustomSymbolInBed");

  for (int n = 0; n != customSymbolsInBedNodes.size(); n++) {
    QDomElement e = customSymbolsInBedNodes.item(n).toElement();
    bed->addCustomSymbol(_project->getCustomSymbol(e.attribute("customSymbolId").toInt()));
    }*/
}

void XMLInterface::loadGrainSizeForBed(Bed* bed, QDomElement& bedE) {
  (void) bed;
  (void) bedE;
  /*  if (bedE.hasAttribute("grainSizeMode")) {
    if (bedE.attribute("grainSizeMode").toInt() == (int) CarbonateGrainSizeMode) {
      bed->setGrainSizeMode(CarbonateGrainSizeMode);
      if (bedE.hasAttribute("baseCarbonateGrainSizeId")) {
	bed->setBaseCarbonateGrainSize(_project->getCarbonateGrainSize(bedE.attribute("baseCarbonateGrainSizeId").toInt()));
      }
      if (bedE.hasAttribute("topCarbonateGrainSizeId")) {
	bed->setTopCarbonateGrainSize(_project->getCarbonateGrainSize(bedE.attribute("topCarbonateGrainSizeId").toInt()));
      }
    }
    if (bedE.attribute("grainSizeMode").toInt() == (int) ClasticGrainSizeMode) {
      bed->setGrainSizeMode(ClasticGrainSizeMode);
      if (bedE.hasAttribute("baseClasticGrainSizeId")) {
	bed->setBaseClasticGrainSize(_project->getClasticGrainSize(bedE.attribute("baseClasticGrainSizeId").toInt()));
      }
      if (bedE.hasAttribute("topClasticGrainSizeId")) {
	bed->setTopClasticGrainSize(_project->getClasticGrainSize(bedE.attribute("topClasticGrainSizeId").toInt()));
      }
    }
    }*/
}

void XMLInterface::loadBed(Bed* bed, QDomElement& bedE) {
  (void) bed;
  (void) bedE;
  /*  bed->setDescription(bedE.attribute("description"));

  bed->getHeight()->setValue(bedE.attribute("heightValue").toInt());
  bed->getHeight()->setUnit(_project->getLengthUnit(bedE.attribute("heightLengthUnitId").toInt()));

  if (bedE.hasAttribute("grainSizeMode")) {
    bed->setGrainSizeMode((GrainSizeModes) (bedE.attribute("grainSizeMode").toInt()));
  }
  if (bedE.hasAttribute("faciesId")) {
    bed->setFacies(_project->getFacies(bedE.attribute("faciesId").toInt()));
  }
  if (bedE.hasAttribute("outcropQualityId")) {
    bed->setOutcropQuality(_project->getOutcropQuality(bedE.attribute("outcropQualityId").toInt()));
  }
  if (bedE.hasAttribute("colorId")) {
    bed->setColor(_project->getColor(bedE.attribute("colorId").toInt()));
  }
  if (bedE.hasAttribute("lithologicalUnitId")) {
    bed->setLithologicalUnit(_project->getLithologicalUnit(bedE.attribute("lithologicalUnitId").toInt()));
  }
  if (bedE.hasAttribute("lithologyId")) {
    bed->setLithology(_project->getLithology(bedE.attribute("lithologyId").toInt()));
  }
  if (bedE.hasAttribute("beddingTypeId")) {
    bed->setBeddingType(_project->getBeddingType(bedE.attribute("beddingTypeId").toInt()));
  }
  if (bedE.hasAttribute("topBoundaryTypeId")) {
    bed->setTopBoundaryType(_project->getBoundaryType(bedE.attribute("topBoundaryTypeId").toInt()));
  }

  loadGrainSizeForBed(bed, bedE);
  loadFossilsInBed(bed, bedE);
  loadSedimentStructuresInBed(bed, bedE);
  loadCustomSymbolsInBed(bed, bedE);*/
}

void XMLInterface::loadProfile(Profile* profile, QDomElement& profileE) {
  (void) profile;
  (void) profileE;
  /*  profile->setName(profileE.attribute("name"));
  profile->setDescription(profileE.attribute("description"));
  profile->setMaxSymbolSize(profileE.attribute("maxSymbolSize").toInt());
  profile->setScale(profileE.attribute("scale").toInt());
  profile->setCellSize(profileE.attribute("cellSize").toInt());
  profile->setLegendColumns(profileE.attribute("legendColumns").toInt());
  profile->setShowHeight((bool)profileE.attribute("showHeight").toInt());
  profile->setShowBedNumbers((bool)profileE.attribute("showBedNumbers").toInt());
  profile->setShowLithology((bool)profileE.attribute("showLithology").toInt());
  profile->setShowBeddingType((bool)profileE.attribute("showBeddingType").toInt());
  profile->setShowTopBoundaryType((bool)profileE.attribute("showTopBoundaryType").toInt());
  profile->setShowFossils((bool)profileE.attribute("showFossils").toInt());
  profile->setShowSedimentStructures((bool)profileE.attribute("showSedimentStructures").toInt());
  profile->setShowGrainSize((bool)profileE.attribute("showGrainSize").toInt());
  profile->setShowCustomSymbols((bool)profileE.attribute("showCustomSymbols").toInt());
  profile->setShowNotes((bool)profileE.attribute("showNotes").toInt());
  profile->setShowColor((bool)profileE.attribute("showColor").toInt());
  profile->setShowFacies((bool)profileE.attribute("showFacies").toInt());
  profile->setShowLithologicalUnit((bool)profileE.attribute("showLithologicalUnit").toInt());
  profile->setShowOutcropQuality((bool)profileE.attribute("showOutcropQuality").toInt());
  profile->setShowHeightMarks((bool)profileE.attribute("showHeightMarks").toInt());

  if (profileE.hasAttribute("defaultLengthUnitId")) {
    profile->setDefaultUnit(_project->getLengthUnit(profileE.attribute("defaultLengthUnitId").toInt()));
  }

  LengthMeasurement* big = profile->getBigMarksDistance();
  LengthMeasurement* small = profile->getSmallMarksDistance();

  if (profileE.hasAttribute("bigMarksDistanceValue")) {
    big->setValue(profileE.attribute("bigMarksDistanceValue").toInt());
  }
  if (profileE.hasAttribute("bigMarksDistanceLengthUnitId")) {
    big->setUnit(_project->getLengthUnit(profileE.attribute("bigMarksDistanceLengthUnitId").toInt()));
  }

  if (profileE.hasAttribute("smallMarksDistanceValue")) {
    small->setValue(profileE.attribute("smallMarksDistanceValue").toInt());
  }
  if (profileE.hasAttribute("smallMarksDistanceLengthUnitId")) {
    small->setUnit(_project->getLengthUnit(profileE.attribute("smallMarksDistanceLengthUnitId").toInt()));
  }

  QDomNodeList samples = profileE.elementsByTagName("Samples");

  if (samples.size() == 1) {
    QDomElement g = samples.at(0).toElement();

    QDomNodeList lst = g.elementsByTagName("Sample");

    for (int i = 0; i < lst.size(); i++) {
      QDomElement e = lst.at(i).toElement();
      Sample* s = profile->createSample(e.attribute("id").toInt());
      s->setName(e.attribute("name"));
      s->setDescription(e.attribute("description"));
    }
  }

  QDomNodeList images = profileE.elementsByTagName("Images");

  if (images.size() == 1) {
    QDomElement g = images.at(0).toElement();

    QDomNodeList lst = g.elementsByTagName("Image");

    for (int i = 0; i < lst.size(); i++) {
      QDomElement e = lst.at(i).toElement();
      Image* s = profile->createImage(e.attribute("id").toInt());
      s->setName(e.attribute("name"));
      s->setDescription(e.attribute("description"));
      s->setFileName(e.attribute("fileName"));
    }
  }

  QDomNodeList beds = profileE.elementsByTagName("Bed");
  for (int bi = 0; bi < beds.size(); bi++) {
    QDomElement bedE = beds.at(bi).toElement();
    Bed* bed = profile->createBed(bedE.attribute("id").toInt(),
				  bedE.attribute("position").toInt());
    loadBed(bed, bedE);
    }*/
}

void XMLInterface::loadProfiles() {
  /*  QDomNodeList lData = _doc.documentElement().elementsByTagName("Data");
  if (lData.size() == 1) {
    _dataE = lData.at(0).toElement();

    QDomNodeList profiles = _dataE.elementsByTagName("Profile");
    for (int i = 0; i < profiles.size(); i++) {
      QDomElement profileE = profiles.at(i).toElement();
      Profile* profile = _project->createProfile(QVariant(profileE.attribute("id")).toInt());
      loadProfile(profile, profileE);
    }
    }*/
}

void XMLInterface::loadProfileCorrelations() {
  /*  QDomNodeList lData = _doc.documentElement().elementsByTagName("Data");
  if (lData.size() == 1) {
    _dataE = lData.at(0).toElement();
    
    QDomNodeList corrs = _dataE.elementsByTagName("ProfileCorrelations");

    if (corrs.size() == 1) {
      QDomElement corrsE = corrs.at(0).toElement();

      QDomNodeList corrNodes = corrsE.elementsByTagName("ProfileCorrelation");
      for (int i = 0; i < corrNodes.size(); i++) {
	QDomElement corrE = corrNodes.at(i).toElement();
	ProfileCorrelation* c = _project->createProfileCorrelation(corrE.attribute("id").toInt());
	c->setName(corrE.attribute("name"));
	c->setDescription(corrE.attribute("description"));

	QDomNodeList l = corrE.elementsByTagName("BedCorrelation");
	for (int j =0 ; j < l.size(); j++) {
	  QDomElement e = l.at(j).toElement();
	  BedCorrelation* bc = c->createBedCorrelation(e.attribute("id").toInt());
	  loadBedCorrelation(bc, e);
	}
      }
    }
    }*/
}

void XMLInterface::loadBedCorrelation(BedCorrelation* bc, QDomElement& e) {
  (void) bc;
  (void) e;
  /*  if (!bc) {
    return;
  }

  if (e.hasAttribute("leftProfileId")) {
    Profile* leftP = _project->getProfile(e.attribute("leftProfileId").toInt());
    if (leftP) {
      if (e.hasAttribute("leftBedId")) {
	bc->setLeftBed(leftP->getBedById(e.attribute("leftBedId").toInt()));
      }
    }
  }

  if (e.hasAttribute("rightProfileId")) {
    Profile* rightP = _project->getProfile(e.attribute("rightProfileId").toInt());
    if (rightP) {
      if (e.hasAttribute("rightBedId")) {
	bc->setRightBed(rightP->getBedById(e.attribute("rightBedId").toInt()));
      }
    }
    }*/
}

bool XMLInterface::load(Project* p, const QString& path) {
  _project = p;
  if (!p) {
    return false;
  }
  _project->setPath(path);

  _doc = QDomDocument("ProfileLogger");
  QFile f(path);

  if (!f.open(QIODevice::ReadOnly)) {
    return false;
  }

  if (!_doc.setContent(&f)) {
    f.close();
    return false;
  }

  f.close();

  /*  loadMetadata();
  loadProfiles();
  loadProfileCorrelations();
  */
  return true;
}

bool XMLInterface::getProjectPathFromUserAndSave() {
  QString path = QFileDialog::getSaveFileName((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
					      tr("Save Project"),
					      QDir::currentPath(),
					      "ProfileLogger Files *.plf");

  if (path.isEmpty()) {
    QMessageBox::information((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
			     tr("Not Saved"),
			     tr("Not saved because no file name provided."));
    return false;
  }

  _project->setPath(path);
  return save(_project);
}
