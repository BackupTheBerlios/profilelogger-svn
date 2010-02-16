/* 
 * File:   Profile.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 19:44
 */

#include "Profile.h"

#include <QApplication>
#include <QMessageBox>

#include "Project.h"
#include "MainWindow.h"
#include "Bed.h"
#include "Sample.h"
#include "Image.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "LengthUnit.h"
#include "LengthMeasurement.h"
#include "CsvInterface.h"
#include "CsvProfileImportSettings.h"
#include "CsvProfileImportSettingsDialog.h"

Profile::Profile(Project* project,
		 int id,
		 const QString& name,
		 const QString& description,
		 const bool isInDatabase,
		 int scale,
		 int legendColumns,
		 bool showHeight,
		 bool showBedNumbers,
		 bool showLithology,
		 bool showBeddingType,
		 bool showTopBoundaryType,
		 bool showFossils,
		 bool showSedimentStructures,
		 bool showGrainSize,
		 bool showCustomSymbols,
		 bool showNotes,
		 bool showColor,
		 bool showFacies,
		 bool showLithologicalUnit,
		 bool showOutcropQuality,
		 bool showHeightMarks,
		 LengthUnit* defaultUnit)
  : DatasetInProject(project, 
		     id, 
		     name, 
		     description,
		     isInDatabase),
    _maxSymbolSize(50),
    _scale(scale),
    _cellSize(30),
    _bigMarksDistance(0),
    _smallMarksDistance(0),
    _legendColumns(legendColumns),
    _defaultUnit(defaultUnit),
    _showHeight(showHeight),
    _showBedNumbers(showBedNumbers),
    _showLithology(showLithology),
    _showBeddingType(showBeddingType),
    _showTopBoundaryType(showTopBoundaryType),
    _showFossils(showFossils),
    _showSedimentStructures(showSedimentStructures),
    _showGrainSize(showGrainSize),
    _showCustomSymbols(showCustomSymbols),
    _showNotes(showNotes),
    _showColor(showColor),
    _showFacies(showFacies),
    _showLithologicalUnit(showLithologicalUnit),
    _showOutcropQuality(showOutcropQuality),
    _showHeightMarks(showHeightMarks) {
  _bigMarksDistance = new LengthMeasurement();
  _bigMarksDistance->setValue(1000);
  _bigMarksDistance->setUnit((static_cast<ProfileLogger*> (QApplication::instance()))->getProject()->getDefaultLengthUnit());
  _smallMarksDistance = new LengthMeasurement();
  _smallMarksDistance->setValue(100);
  _smallMarksDistance->setUnit((static_cast<ProfileLogger*> (QApplication::instance()))->getProject()->getDefaultLengthUnit());
    }

Profile::~Profile() {
  _beds.clear();
  _samples.clear();
  _images.clear();
}

Bed* Profile::createBed(int position) {
  if (position > 0) {
    _beds.insert(position, new Bed(0, 0, position, QString::number(position)));
  } else {
    _beds.append(new Bed(this, 0, position, QString::number(position)));
  }

  renumberBeds();
  Bed* b = getBedByPosition(position);
    
  if (hasDefaultUnit()) {
    b->getHeight()->setUnit(getDefaultUnit());
  }

  return b;
}

Bed* Profile::getBedById(int id) {
  for (int i = 0; i < _beds.size(); i++) {
    if (_beds.at(i)->getId() == id) {
      return _beds.at(i);
    }
  }

  return 0;
}

Bed* Profile::getBedByPosition(int position) {
  return _beds.at(position);
}

void Profile::renumberBeds() {
  for (int i = 0; i < _beds.size(); i++) {
    _beds.at(i)->setPosition(i + 1);
  }
}

void Profile::moveBedUp(Bed* b) {
  int currPos = _beds.indexOf(b);
  if (currPos >= _beds.size() - 1) {
    return; // can't move above top
  }
  _beds.swap(currPos, currPos + 1);
  renumberBeds();
}

void Profile::moveBedDown(Bed* b) {
  int currPos = _beds.indexOf(b);
  if (currPos == 0) {
    return; // can't move below bottom
  }
  _beds.swap(currPos, currPos - 1);
  renumberBeds();
}

void Profile::deleteBed(Bed* b) {
  if (_beds.contains(b)) {
    _beds.removeAll(b);
    renumberBeds();
  }
}

void Profile::deleteBedsAbove(Bed* bed) {
  int lastSavePos = bed->getPosition();
  QList<Bed*> delme;

  for (QList<Bed*>::iterator it = getFirstBed(); it != getLastBed(); it++) {
    Bed* b = *it;

    if (b->getPosition() > lastSavePos) {
      delme << b;
    }
  }

  for (QList<Bed*>::iterator it = delme.begin(); it != delme.end(); it++) {
    deleteBed(*it);
  }
}

void Profile::deleteBedsBelow(Bed* bed) {
  int lastSavePos = bed->getPosition();
  QList<Bed*> delme;

  for (QList<Bed*>::iterator it = getFirstBed(); it != getLastBed(); it++) {
    Bed* b = *it;

    if (b->getPosition() < lastSavePos) {
      delme << b;
    }
  }

  for (QList<Bed*>::iterator it = delme.begin(); it != delme.end(); it++) {
    deleteBed(*it);
  }
}

QString Profile::makeToolTipText(const bool withDatasetName) {
  QStringList ret;
  if (withDatasetName) {
    ret << QObject::tr("Profile:");
  }

  ret << QObject::tr("Id: %1").arg(getId())
      << QObject::tr("Name: %1").arg(getName())
      << QObject::tr("Description: %1").arg(getDescription())
      << QObject::tr("Scale: 1:%2").arg(getScale())
      << QObject::tr("Cell Size: %1").arg(getCellSize())
      << QObject::tr("Columns in Legend: %1").arg(getLegendColumns())
      << QObject::tr("Sample count: %1").arg(getSampleCount());

  if (hasDefaultUnit()) {
    ret << QObject::tr("Default Unit: %1").arg(getDefaultUnit()->getName());
  }

  return ret.join("\n");
}

int Profile::getHeightInMillimetres() {
  int ret = 0;

  for (QList<Bed*>::iterator it = _beds.begin(); it != _beds.end(); it++) {
    LengthMeasurement* m = (*it)->getHeight();
    if (m) {
      ret += m->getMillimetres();
    }
  }

  return ret;
}

void Profile::splitAtBed(Bed* b) {
  if (!b) {
    return;
  }

  Profile* bottom = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject()->createProfile();
  Profile* top = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject()->createProfile();

  bottom->setName(QObject::tr("Bottom of %1").arg(getName()));
  bottom->setLegendColumns(getLegendColumns());
  bottom->setMaxSymbolSize(getMaxSymbolSize());
  bottom->setScale(getScale());

  top->setName(QObject::tr("Top of %1").arg(getName()));
  top->setLegendColumns(getLegendColumns());
  top->setMaxSymbolSize(getMaxSymbolSize());
  top->setScale(getScale());

  QList<Bed*>::iterator it = getFirstBed();

  int splitBedId = b->getId();

  int pos = 0;
  while (it != getLastBed()) {
    Bed * n = bottom->createBed(pos);
    Bed* o = *it;

    if (o) {
      n->getHeight()->setValue(o->getHeight()->getValue());
      n->getHeight()->setUnit(o->getHeight()->getUnit());
      n->setName(o->getName());
      n->setLithology(o->getLithology());
      n->setBaseCarbonateGrainSize(o->getBaseCarbonateGrainSize());
      n->setBaseClasticGrainSize(o->getBaseClasticGrainSize());
      n->setBeddingType(o->getBeddingType());
      n->setColor(o->getColor());
      n->setDescription(o->getDescription());
      n->setFacies(o->getFacies());
      n->setGrainSizeMode(o->getGrainSizeMode());
      n->setOutcropQuality(o->getOutcropQuality());
      n->setTopBoundaryType(o->getTopBoundaryType());
      n->setTopCarbonateGrainSize(o->getTopCarbonateGrainSize());
      n->setTopClasticGrainSize(o->getTopClasticGrainSize());

      for (QList<Fossil*>::iterator it = o->getFirstFossil();
	   it != o->getLastFossil();
	   it++) {
	n->addFossil(*it);
      }

      for (QList<SedimentStructure*>::iterator it = o->getFirstSedimentStructure();
	   it != o->getLastSedimentStructure();
	   it++) {
	n->addSedimentStructure(*it);
      }

      for (QList<CustomSymbol*>::iterator it = o->getFirstCustomSymbol();
	   it != o->getLastCustomSymbol();
	   it++) {
	n->addCustomSymbol(*it);
      }
    }
    it++;
    pos++;

    if (o->getId() == splitBedId) {
      break;
    }
  }

  pos = 0;
  while (it != getLastBed()) {
    Bed * n = top->createBed(pos);
    Bed* o = *it;

    if (o) {
      n->getHeight()->setValue(o->getHeight()->getValue());
      n->getHeight()->setUnit(o->getHeight()->getUnit());
      n->setName(o->getName());
      n->setLithology(o->getLithology());
      n->setBaseCarbonateGrainSize(o->getBaseCarbonateGrainSize());
      n->setBaseClasticGrainSize(o->getBaseClasticGrainSize());
      n->setBeddingType(o->getBeddingType());
      n->setColor(o->getColor());
      n->setDescription(o->getDescription());
      n->setFacies(o->getFacies());
      n->setGrainSizeMode(o->getGrainSizeMode());
      n->setOutcropQuality(o->getOutcropQuality());
      n->setTopBoundaryType(o->getTopBoundaryType());
      n->setTopCarbonateGrainSize(o->getTopCarbonateGrainSize());
      n->setTopClasticGrainSize(o->getTopClasticGrainSize());

      for (QList<Fossil*>::iterator it = o->getFirstFossil();
	   it != o->getLastFossil();
	   it++) {
	n->addFossil(*it);
      }

      for (QList<SedimentStructure*>::iterator it = o->getFirstSedimentStructure();
	   it != o->getLastSedimentStructure();
	   it++) {
	n->addSedimentStructure(*it);
      }

      for (QList<CustomSymbol*>::iterator it = o->getFirstCustomSymbol();
	   it != o->getLastCustomSymbol();
	   it++) {
	n->addCustomSymbol(*it);
      }
    }
    it++;
    pos++;
  }
}

Sample* Profile::createSample() {
  _samples.append(new Sample(0, QObject::tr("New Sample"), QString::null, this));
  return _samples.last();
}

Sample* Profile::getSample(int id) {
  for (int i = 0; i < _samples.size(); i++) {
    Sample* s = _samples.at(i);

    if (s->getId() == id) {
      return s;
    }
  }

  return 0;
}

QList<Sample*>::iterator Profile::getFirstSample() {
  return _samples.begin();
}

QList<Sample*>::iterator Profile::getLastSample() {
  return _samples.end();
}

void Profile::deleteSample(Sample* s) {
  if (!s) {
    return;
  }

  int i = _samples.indexOf(s);

  if (-1 == i) {
    return;
  }

  Sample* t = _samples.takeAt(i);

  if (t) {
    delete t;
  }
}

int Profile::getSampleCount() {
  return _samples.size();
}

Image* Profile::createImage() {
  _images.append(new Image(this,
			   0, 
			   QObject::tr("New Image"), 
			   QString::null,
			   QString::null));
  return _images.last();
}

Image* Profile::getImage(int id) {
  for (int i = 0; i < _images.size(); i++) {
    Image* img = _images.at(i);

    if (img->getId() == id) {
      return img;
    }
  }

  return 0;
}

QList<Image*>::iterator Profile::getFirstImage() {
  return _images.begin();
}

QList<Image*>::iterator Profile::getLastImage() {
  return _images.end();
}

void Profile::deleteImage(Image* s) {
  if (!s) {
    return;
  }

  int i = _images.indexOf(s);

  if (-1 == i) {
    return;
  }

  Image* img = _images.takeAt(i);

  if (img) {
    delete img;
  }
}

int Profile::getImageCount() {
  return _images.size();
}

qreal Profile::getScaleFactor() {
  if (getScale() <= 0) {
    return 1.0;
  }

  return (qreal) getCellSize() / (qreal) getScale();
}

qreal Profile::getScaledHeight() {
  return getHeightInMillimetres() * getScaleFactor();
}

Bed* Profile::copyBed(Bed* other, int newId, int newPosition) {
  (void) other;
  (void) newId;
  (void) newPosition;
  /*  Bed* bed = createBed(newId, newPosition);

      bed->getHeight()->setValue(other->getHeight()->getValue());
      bed->getHeight()->setUnit(other->getHeight()->getUnit());
      bed->setName(other->getName());
      bed->setLithology(other->getLithology());
      bed->setLithologicalUnit(other->getLithologicalUnit());
      bed->setBaseCarbonateGrainSize(other->getBaseCarbonateGrainSize());
      bed->setBaseClasticGrainSize(other->getBaseClasticGrainSize());
      bed->setBeddingType(other->getBeddingType());
      bed->setColor(other->getColor());
      bed->setDescription(other->getDescription());
      bed->setFacies(other->getFacies());
      bed->setGrainSizeMode(other->getGrainSizeMode());
      bed->setOutcropQuality(other->getOutcropQuality());
      bed->setTopBoundaryType(other->getTopBoundaryType());
      bed->setTopCarbonateGrainSize(other->getTopCarbonateGrainSize());
      bed->setTopClasticGrainSize(other->getTopClasticGrainSize());

      for (QList<Fossil*>::iterator it = other->getFirstFossil();
      it != other->getLastFossil();
      it++) {
      bed->addFossil(*it);
      }

      for (QList<SedimentStructure*>::iterator it = other->getFirstSedimentStructure();
      it != other->getLastSedimentStructure();
      it++) {
      bed->addSedimentStructure(*it);
      }

      for (QList<CustomSymbol*>::iterator it = other->getFirstCustomSymbol();
      it != other->getLastCustomSymbol();
      it++) {
      bed->addCustomSymbol(*it);
      }

      return bed;*/
  return 0;
}

void Profile::copyData(Profile* other) {
  if (!other) {
    return;
  }

  setName(QObject::tr("Copy of %1").arg(other->getName()));
  setDescription(other->getDescription());
  setMaxSymbolSize(other->getMaxSymbolSize());
  setScale(other->getScale());
  setCellSize(other->getCellSize());
  getBigMarksDistance()->setValue(other->getBigMarksDistance()->getValue());
  getBigMarksDistance()->setUnit(other->getBigMarksDistance()->getUnit());
  getSmallMarksDistance()->setValue(other->getSmallMarksDistance()->getValue());
  getSmallMarksDistance()->setUnit(other->getSmallMarksDistance()->getUnit());
  setLegendColumns(other->getLegendColumns());

  for (QList<Bed*>::iterator it = other->getFirstBed(); it != other->getLastBed(); it++) {
    copyBed(*it);
  }

  for (QList<Sample*>::iterator it = other->getFirstSample(); it != other->getLastSample(); it++) {
    Sample* s = createSample();
    s->setName((*it)->getName());
    s->setDescription((*it)->getDescription());
  }

  for (QList<Image*>::iterator it = other->getFirstImage(); it != other->getLastImage(); it++) {
    Image* i = createImage();
    i->setName((*it)->getName());
    i->setDescription((*it)->getDescription());
  }
}

void Profile::importBedsFromCsvFile() {
  CsvProfileImportSettings s;

  CsvProfileImportSettingsDialog* dlg = new CsvProfileImportSettingsDialog((static_cast<ProfileLogger*> (QApplication::instance()))->getMainWindow(), &s);

  if (dlg->exec() != QDialog::Accepted) {
    return;
  }

  QFileInfo fi(s.getFileName());

  if (!fi.isReadable()) {
    QMessageBox::warning((static_cast<ProfileLogger*> (QApplication::instance()))->getMainWindow(),
			 QObject::tr("File not readable"),
			 QObject::tr("File not readable: %1").arg(fi.absoluteFilePath()));
    return;
  }

  CsvInterface cif(QApplication::instance());
  cif.setFileName(s.getFileName());

  QList<QStringList> data = cif.getData(s.getSepChar());

  if (s.getIgnoreFirstLine()) {
    data.pop_front();
  }

  for (QList<QStringList>::iterator it = data.begin(); it != data.end(); it++) {
    QStringList buf = *it;

    Bed* b = createBed();
    b->getHeight()->setValue(buf[0].toInt());
    b->setLithology((static_cast<ProfileLogger*> (QApplication::instance()))->getProject()->getLithology(buf[1].toInt()));
  }
}
