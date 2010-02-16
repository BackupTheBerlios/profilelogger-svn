/*
 * File:   LithologyEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "LithologyEditorDialog.h"

#include <QLayout>

#include "Lithology.h"
#include "Settings.h"
#include "ProfileLogger.h"
#include "GrainSizeSelectorWidget.h"
#include "LithologyManager.h"
#include "DatabaseError.h"
#include "DatabaseErrorDialog.h"

LithologyEditorDialog::LithologyEditorDialog(QWidget* parent, Lithology* p)
  : DatasetInProjectWithFileNameEditorDialog(parent, p) {
  Q_ASSERT(p->hasProject());
  setDataManager(new LithologyManager(this,
				      getPostgres(),
				      getProfileLoggerDatabase()));
  
  addMainPage(tr("Lithology"));
  addIdLabel();
  addNameEdit();
  addFileNameBrowser(tr("Pattern"),
		     (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getLithologiesPatternPath());

  _grainSizeW = new GrainSizeSelectorWidget(getMainPage());

  QGridLayout* l = ((QGridLayout*) (getMainPage()->layout()));

  l->addWidget(new QLabel(tr("Default Grain Size"), getMainPage()), r, lC);
  l->addWidget(_grainSizeW, r, wC);
  r++;

  connect(_grainSizeW, SIGNAL(grainSizeModeChanged(GrainSizeModes)), this, SLOT(slotDefaultGrainSizeModeChanged(GrainSizeModes)));
  connect(_grainSizeW, SIGNAL(carbonateGrainSizeChanged(CarbonateGrainSize*)), this, SLOT(slotDefaultCarbonateGrainSizeChanged(CarbonateGrainSize*)));
  connect(_grainSizeW, SIGNAL(clasticGrainSizeChanged(ClasticGrainSize*)), this, SLOT(slotDefaultClasticGrainSizeChanged(ClasticGrainSize*)));

  _grainSizeW->setGrainSizeMode(getLithology()->getDefaultGrainSizeMode());
  _grainSizeW->setClasticGrainSize(getLithology()->getDefaultClasticGrainSize());
  _grainSizeW->setCarbonateGrainSize(getLithology()->getDefaultCarbonateGrainSize());

  addDescriptionEdit();
  addButtons();

  emit showDatasetRequest(getLithology());
  slotShowDataset(getLithology());
}

LithologyEditorDialog::~LithologyEditorDialog() {
}

Lithology* LithologyEditorDialog::getLithology() {
  return (Lithology*) getDataset();
}

void LithologyEditorDialog::slotDefaultGrainSizeModeChanged(GrainSizeModes m) {
  getLithology()->setDefaultGrainSizeMode(m);
}

void LithologyEditorDialog::slotDefaultCarbonateGrainSizeChanged(CarbonateGrainSize* s) {
  getLithology()->setDefaultCarbonateGrainSize(s);
}

void LithologyEditorDialog::slotDefaultClasticGrainSizeChanged(ClasticGrainSize* s) {
  getLithology()->setDefaultClasticGrainSize(s);
}

void LithologyEditorDialog::accept() {
  try {
    begin();
    getLithologyManager()->save(getLithology());
    commit();
    done(QDialog::Accepted);
  }
  catch(DatabaseError e) {
    DatabaseErrorDialog dlg(QApplication::activeWindow(), e);
    dlg.exec();

    try {
      rollback();
    }
    catch(DatabaseError e) {
      DatabaseErrorDialog dlg(QApplication::activeWindow(), e);
      dlg.exec();
    }
  }  
}

LithologyManager* LithologyEditorDialog::getLithologyManager() {
  return (LithologyManager*)getDataManager();
}
