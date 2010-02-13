/*
 * File:   BedCorrelationEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "BedCorrelationEditorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QGroupBox>
#include <QApplication>

#include "BedCorrelation.h"
#include "NameEdit.h"
#include "ProfileItemModel.h"
#include "ProfileItemView.h"
#include "BedItemModel.h"
#include "BedItemView.h"
#include "ProfileLogger.h"
#include "Bed.h"
#include "Profile.h"
#include "NameEdit.h"

BedCorrelationEditorDialog::BedCorrelationEditorDialog(QWidget* parent, BedCorrelation* p)
  : DatasetEditorDialog(parent, p) {
  addMainPage(tr("Bed Correlation"));
  addIdLabel();
  addNameEdit();
  addDescriptionEdit();
  addButtons();
  getNameEdit()->setEnabled(false);

  setupBedSelectors();

  emit showDatasetRequest(getBedCorrelation());
  slotShowDataset(getBedCorrelation());
  slotShowBedCorrelation(getBedCorrelation());

  connect(_leftProfileV, SIGNAL(currentProfileChanged(Profile*)), _leftBedV, SLOT(slotCurrentProfileChanged(Profile*)));
  connect(_leftProfileV, SIGNAL(currentProfileChanged(Profile*)), _leftBedM, SLOT(slotCurrentProfileChanged(Profile*)));
  connect(_rightProfileV, SIGNAL(currentProfileChanged(Profile*)), _rightBedV, SLOT(slotCurrentProfileChanged(Profile*)));
  connect(_rightProfileV, SIGNAL(currentProfileChanged(Profile*)), _rightBedM, SLOT(slotCurrentProfileChanged(Profile*)));
  connect(_leftBedV, SIGNAL(currentBedChanged(Bed*)), this, SLOT(slotLeftBedChanged(Bed*)));
  connect(_rightBedV, SIGNAL(currentBedChanged(Bed*)), this, SLOT(slotRightBedChanged(Bed*)));
}

BedCorrelationEditorDialog::~BedCorrelationEditorDialog() {
}

BedCorrelation* BedCorrelationEditorDialog::getBedCorrelation() {
  return (BedCorrelation*) getDataset();
}

void BedCorrelationEditorDialog::setupBedSelectors() {
  QWidget* w = new QWidget(getMainPage());

  QGridLayout* l = new QGridLayout(w);
  w->setLayout(l);

  _leftProfileM = new ProfileItemModel(this);
  _leftProfileV = new ProfileItemView(this, _leftProfileM);
  _rightProfileM = new ProfileItemModel(this);
  _rightProfileV = new ProfileItemView(this, _rightProfileM);

  _leftProfileV->setEnabled(true);
  _leftProfileV->setContextMenuPolicy(Qt::NoContextMenu);
  _rightProfileV->setEnabled(true);
  _rightProfileV->setContextMenuPolicy(Qt::NoContextMenu);
    
  _leftBedM = new BedItemModel(this);
  _leftBedV = new BedItemView(this, _leftBedM);
  _rightBedM = new BedItemModel(this);
  _rightBedV = new BedItemView(this, _rightBedM);

  _leftBedV->setEnabled(true);
  _leftBedV->setContextMenuPolicy(Qt::NoContextMenu);
  _rightBedV->setEnabled(true);
  _rightBedV->setContextMenuPolicy(Qt::NoContextMenu);

  l->addWidget(_leftProfileV, 0, 0);
  l->addWidget(_rightProfileV, 0, 1);
  l->addWidget(_leftBedV, 1, 0);
  l->addWidget(_rightBedV, 1, 1);

  ((QGridLayout*)(getMainPage()->layout()))->addWidget(w, r, wC);
  r++;
}

void BedCorrelationEditorDialog::slotShowBedCorrelation(BedCorrelation* c) {
  _leftProfileM->slotCurrentProjectChanged((static_cast<ProfileLogger*>(QApplication::instance()))->getProject());
  _rightProfileM->slotCurrentProjectChanged((static_cast<ProfileLogger*>(QApplication::instance()))->getProject());

  if (c->hasLeftBed()) {
    Bed* left = c->getLeftBed();
    if (left->hasProfile()) {
      Profile* p = left->getProfile();
      _leftProfileV->selectProfile(p);

      _leftBedM->slotCurrentProfileChanged(p);
      _leftBedV->slotCurrentProfileChanged(p);
      _leftBedV->selectBed(left);
    }
  }

  if (c->hasRightBed()) {
    Bed* right = c->getRightBed();
    if (right->hasProfile()) {
      Profile* p = right->getProfile();
      _rightProfileV->selectProfile(p);

      _rightBedM->slotCurrentProfileChanged(p);
      _rightBedV->slotCurrentProfileChanged(p);
      _rightBedV->selectBed(right);
    }
  }      
}

void BedCorrelationEditorDialog::slotLeftBedChanged(Bed* b) {
  getBedCorrelation()->setLeftBed(b);
  getNameEdit()->setText(getBedCorrelation()->getName());
}

void BedCorrelationEditorDialog::slotRightBedChanged(Bed* b) {
  getBedCorrelation()->setRightBed(b);
  getNameEdit()->setText(getBedCorrelation()->getName());
}
