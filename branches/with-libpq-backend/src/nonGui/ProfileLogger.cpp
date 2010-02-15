/* 
 * File:   ProfileLogger.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 19:32
 */

#include "ProfileLogger.h"

#include <QAction>
#include <QMessageBox>
#include <QKeySequence>
#include <QFileDialog>
#include <QGraphicsScene>
#include <QMessageBox>
#include <QMainWindow>
#include <QFileInfo>
#include <QTranslator>
#include <QDebug>

#include "MainWindow.h"

#include "DatabaseError.h"
#include "DatabaseErrorDialog.h"

#include "ProfileLoggerDatabase.h"
#include "Postgres.h"
#include "DatabaseConnectionDialog.h"

#include "Version.h"
#include "Project.h"
#include "XMLInterface.h"
#include "ProfileItemModel.h"
#include "BedItemModel.h"
#include "OutcropQualityItemModel.h"
#include "ColorItemModel.h"
#include "LithologyItemModel.h"
#include "BeddingTypeItemModel.h"
#include "BoundaryTypeItemModel.h"
#include "CarbonateGrainSizeItemModel.h"
#include "ClasticGrainSizeItemModel.h"
#include "FossilItemModel.h"
#include "FaciesItemModel.h"
#include "ImageItemModel.h"
#include "ProfileCorrelationItemModel.h"
#include "BedCorrelationItemModel.h"
#include "ProjectItemModel.h"

#include "SettingsDialog.h"
#include "Settings.h"
#include "CarbonateGrainSizeView.h"
#include "ClasticGrainSizeItemModel.h"
#include "SedimentStructureItemModel.h"
#include "CustomSymbolItemModel.h"
#include "LithologicalUnitTypeItemModel.h"
#include "LithologicalUnitItemModel.h"
#include "SampleItemModel.h"

ProfileLogger::ProfileLogger(int & argc, char** argv)
  : QApplication(argc, argv),
    _settings(0),
    _xif(0),
    _project(Project()),
    _translator(0),
    _mainW(0),
    _db(0),
    _dbConn(0) {
  _settings = new Settings(this);
  _translator = new QTranslator(this);
  _xif = new XMLInterface(this);
  _db = new ProfileLoggerDatabase(this);
  _dbConn = new Postgres(this);
  setupModels();
  setupActions();
}

void ProfileLogger::loadTranslation() {
  loadTranslation(_settings->getLanguageFile());
}

void ProfileLogger::loadTranslation(const QString& fn) {
  QFileInfo fi(fn);

  if (!fi.isReadable()) {
    QMessageBox::warning(getMainWindow(),
			 tr("Translation file not readable"),
			 tr("Translation file %1 not readable. Defaulting to programmer english :)").arg(fn));
    return;
  }

  _translator->load(fi.fileName(), fi.absolutePath());

  if (_translator->isEmpty()) {
    QMessageBox::warning(getMainWindow(),
			 tr("Translation is empty"),
			 tr("Translation file %1 in directory %2 is empty. Defaulting to programmer english. :)").arg(fi.fileName()).arg(fi.absolutePath()));
    return;
  }

  qDebug() << "Loaded " << fi.fileName() << " from " << fi.absolutePath();

  installTranslator(_translator);
}

ProfileLogger::~ProfileLogger() {
}

void ProfileLogger::setupActions() {
  _openLastProjectA = new QAction(tr("Open Last Project"), this);
  _openLastProjectA->setShortcut(QKeySequence("Ctrl+Shift+o"));
  _openProjectA = new QAction(tr("&Open Project"), this);
  _newProjectA = new QAction(tr("&New Project"), this);
  _saveProjectA = new QAction(tr("&Save Project"), this);
  _saveProjectA->setShortcut(QKeySequence("Ctrl+s"));
  _saveProjectAsA = new QAction(tr("Save Project As..."), this);
  _settingsA = new QAction(tr("Settings..."), this);
  _aboutA = new QAction(tr("About this Program..."), this);
  _aboutQtA = new QAction(tr("About Qt..."), this);
  _quitA = new QAction(tr("Quit"), this);
  _openDatabaseA = new QAction(tr("Open Database..."), this);
  _openDatabaseA->setShortcut(QKeySequence("Ctrl+o"));
  _closeDatabaseA = new QAction(tr("Close Database"), this);
  _dropSchemaA = new QAction(tr("Drop Schema..."), this);
  _createSchemaA = new QAction(tr("Create Schema..."), this);
  _insertTemplateDataA = new QAction(tr("Insert Template Data..."), this);

  _reloadBedsA = new QAction(tr("Reload Beds"), this);
  _createBedOnTopA = new QAction(tr("Create Bed On Top..."), this);
  _createBedAboveCurrentBedA = new QAction(tr("Create Bed Above Current Bed..."), this);
  _createBedBelowCurrentBedA = new QAction(tr("Create Bed Below Current Bed..."), this);
  _moveBedUpA = new QAction(tr("Move Current Bed Up"), this);
  _moveBedDownA = new QAction(tr("Move Current Bed Down"), this);
  _editBedA = new QAction(tr("Edit Bed..."), this);
  _deleteBedA = new QAction(tr("Delete Bed..."), this);
  _duplicateBedAndInsertAtTopA = new QAction(tr("Duplicate Current Bed And Insert On Top"), this);
  _splitProfileAtBedA = new QAction(tr("Split Profile At Current Bed"), this);
  _insertProfileAboveBedA = new QAction(tr("Insert Profile Above Current Bed"), this);
  _insertProfileBelowBedA = new QAction(tr("Insert Profile Below Current Bed"), this);
  _deleteBedsAboveBedA = new QAction(tr("Delete Beds Above Current Bed"), this);
  _deleteBedsBelowBelowA = new QAction(tr("Delete Beds Below Current Bed"), this);

  _exportProfileToSvgA = new QAction(tr("Export To SVG..."), this);
  _exportProfileToPdfA = new QAction(tr("Export To PDF..."), this);
  _exportProfileToJpgA = new QAction(tr("Export To JPG..."), this);
  _exportProfileToPngA = new QAction(tr("Export To PNG..."), this);
  _exportProfileToTiffA = new QAction(tr("Export To TIFF..."), this);

  connect(_newProjectA, SIGNAL(activated()), this, SLOT(slotNewProject()));
  connect(_saveProjectA, SIGNAL(activated()), this, SLOT(slotSaveProject()));
  connect(_saveProjectAsA, SIGNAL(activated()), this, SLOT(slotSaveProjectAs()));
  connect(_openProjectA, SIGNAL(activated()), this, SLOT(slotOpenProject()));
  connect(_settingsA, SIGNAL(activated()), this, SLOT(slotManageSettings()));
  connect(_openLastProjectA, SIGNAL(activated()), this, SLOT(slotOpenLastProject()));
  connect(_aboutA, SIGNAL(activated()), this, SLOT(slotAbout()));
  connect(_aboutQtA, SIGNAL(activated()), this, SLOT(slotAboutQt()));
  connect(_quitA, SIGNAL(activated()), this, SLOT(slotQuit()));
  connect(_openDatabaseA, SIGNAL(activated()), this, SLOT(slotOpenDatabase()));
  connect(_closeDatabaseA, SIGNAL(activated()), this, SLOT(slotCloseDatabase()));
  connect(_dropSchemaA, SIGNAL(activated()), this, SLOT(slotDropSchema()));
  connect(_createSchemaA, SIGNAL(activated()), this, SLOT(slotCreateSchema()));
  connect(_insertTemplateDataA, SIGNAL(activated()), this, SLOT(slotInsertTemplateData()));

  connect(_reloadBedsA, SIGNAL(activated()), _bedItemModel, SLOT(reload()));
  connect(_createBedOnTopA, SIGNAL(activated()), _bedItemModel, SLOT(slotCreateBedOnTop()));
  connect(_createBedAboveCurrentBedA, SIGNAL(activated()), _bedItemModel, SLOT(slotCreateBedAboveCurrentBed()));
  connect(_createBedBelowCurrentBedA, SIGNAL(activated()), _bedItemModel, SLOT(slotCreateBedBelowCurrentBed()));
  connect(_editBedA, SIGNAL(activated()), _bedItemModel, SLOT(slotEditCurrentBed()));
  connect(_moveBedUpA, SIGNAL(activated()), _bedItemModel, SLOT(slotMoveCurrentBedUp()));
  connect(_moveBedDownA, SIGNAL(activated()), _bedItemModel, SLOT(slotMoveCurrentBedDown()));
  connect(_duplicateBedAndInsertAtTopA, SIGNAL(activated()), _bedItemModel, SLOT(slotDuplicateCurrentBedAndInsertOnTop()));
  connect(_splitProfileAtBedA, SIGNAL(activated()), _bedItemModel, SLOT(slotSplitProfileAtCurrentBed()));
  connect(_insertProfileBelowBedA, SIGNAL(activated()), _bedItemModel, SLOT(slotInsertProfileBelowCurrentBed()));
  connect(_insertProfileAboveBedA, SIGNAL(activated()), _bedItemModel, SLOT(slotInsertProfileAboveCurrentBed()));

  connect(_deleteBedA, SIGNAL(activated()), _bedItemModel, SLOT(slotDeleteCurrentBed()));
  connect(_deleteBedsAboveBedA, SIGNAL(activated()), _bedItemModel, SLOT(slotDeleteBedsAboveCurrentBed()));
  connect(_deleteBedsBelowBelowA, SIGNAL(activated()), _bedItemModel, SLOT(slotDeleteBedsBelowCurrentBed()));

  _newProjectA->setEnabled(true);
  _saveProjectA->setEnabled(false);
}

void ProfileLogger::setupModels() {
  _profileItemModel = new ProfileItemModel(this);
  _bedItemModel = new BedItemModel(this);
  _outcropQualityItemModel = new OutcropQualityItemModel(this);
  _colorItemModel = new ColorItemModel(this);
  _lithologyItemModel = new LithologyItemModel(this);
  _beddingTypeItemModel = new BeddingTypeItemModel(this);
  _boundaryTypeItemModel = new BoundaryTypeItemModel(this);
  _carbonateGrainSizeItemModel = new CarbonateGrainSizeItemModel(this);
  _clasticGrainSizeItemModel = new ClasticGrainSizeItemModel(this);
  _fossilItemModel = new FossilItemModel(this);
  _sedimentStructureItemModel = new SedimentStructureItemModel(this);
  _customSymbolItemModel = new CustomSymbolItemModel(this);
  _faciesItemModel = new FaciesItemModel(this);
  _lithologicalUnitTypeItemModel = new LithologicalUnitTypeItemModel(this);
  _lithologicalUnitItemModel = new LithologicalUnitItemModel(this);
  _sampleItemModel = new SampleItemModel(this);
  _imageItemModel = new ImageItemModel(this);
  _profileCorrelationItemModel = new ProfileCorrelationItemModel(this);
  _bedCorrelationItemModel = new BedCorrelationItemModel(this);
  _projectItemModel = new ProjectItemModel(this);
}

void ProfileLogger::slotNewProject() {
  QString path = QFileDialog::getSaveFileName(_mainW,
					      tr("New Project"),
					      QDir::currentPath());

  if (path.isEmpty()) {
    return;
  }

  _project = Project();
  _project.setPath(path);
  _saveProjectA->setEnabled(true);
  _saveProjectAsA->setEnabled(true);
  _settings->setLastFile(_project.getPath());
  emit currentProjectChanged(&_project);
}

void ProfileLogger::slotSaveProject() {
  if (_xif->save(&_project)) {
    QMessageBox::information(_mainW, tr("Saved"), tr("Project saved to %1").arg(_project.getPath()));
  } else {
    QMessageBox::critical(_mainW, tr("Saving failed"), tr("Project NOT saved to %1").arg(_project.getPath()));
  }
}

void ProfileLogger::slotSaveProjectAs() {
  QString path = QFileDialog::getSaveFileName(_mainW,
					      tr("Save Project As"),
					      QDir::currentPath());

  if (path.isEmpty()) {
    return;
  }

  _project.setPath(path);
  slotSaveProject();

  _mainW->setWindowTitle(_project.getPath());

  emit currentProjectChanged(&_project);
}

void ProfileLogger::slotOpenProject() {
  QString path = QFileDialog::getOpenFileName(_mainW,
					      tr("Open Project"),
					      QDir::currentPath());

  if (path.isEmpty()) {
    return;
  }

  openProject(path);
}

void ProfileLogger::slotOpenLastProject() {
  QString path = _settings->getLastFile();
  if (path.isEmpty()) {
    return;
  }

  openProject(path);
}

void ProfileLogger::openProject(const QString& path) {
  if (path.isEmpty()) {
    return;
  }

  emit currentProjectChanged(0);

  _project = Project();
  _bedItemModels.clear();
  _profileItemModels.clear();

  if (_xif->load(&_project, path)) {
    emit currentProjectChanged(&_project);
    _saveProjectA->setEnabled(true);
    _saveProjectAsA->setEnabled(true);
    _settings->setLastFile(_project.getPath());
    _mainW->setWindowTitle(_project.getPath());
  } else {
    _settings->setLastFile(QString::null);
    QMessageBox::critical(_mainW,
			  tr("Could Not Open File"),
			  tr("Could not load project from file %1").arg(path));
    _mainW->setWindowTitle(QString::null);
  }
}

void ProfileLogger::slotManageSettings() {
  SettingsDialog* dlg = new SettingsDialog(_mainW);
  if (QDialog::Accepted == dlg->exec()) {     
    loadTranslation();
  }
}

QBrush ProfileLogger::getBrushFromFileName(const QString& dir, const QString& fn) {
  if (fn.isEmpty()) {
    return QBrush();
  }

  if (_brushes.contains(fn)) {
    return _brushes[fn];
  }

  QFileInfo i(QDir(dir), fn);

  QBrush ret;

  if (!i.isReadable()) {
    ret.setColor(Qt::red);
  }

  QImage img(i.canonicalFilePath());

  if (img.isNull()) {
    return ret;
  }

  ret.setTexture(QPixmap::fromImage(img));
  _brushes[fn] = ret;

  return _brushes[fn];
}

QPixmap ProfileLogger::getPixmapFromFileName(const QString& dir, const QString& fn) {
  if (fn.isEmpty()) {
    return QPixmap();
  }

  if (_pixmaps.contains(fn)) {
    return _pixmaps[fn];
  }

  QFileInfo i(QDir(dir), fn);


  if (!i.isReadable()) {
    return QPixmap();
  }

  QPixmap pix;

  if (!pix.load(i.canonicalFilePath())) {
    return QPixmap();
  }

  _pixmaps[fn] = pix;

  return _pixmaps[fn];
}

void ProfileLogger::slotAbout() {
  QMessageBox::about(_mainW,
		     tr("About this program"),
		     tr("<p>For more information please contact the author Johannes Lochmann at <a mailto=\"johannes.lochmann@gmail.com\">johannes.lochmann@gmail.com<a>, have a look at <a href=\"http://profilelogger.sourceforge.net\">http://profilelogger.sourceforge.net</a> or have a look at the authors blog at <a href=\"http://johanneslochmann.blogspot.com\">http://johanneslochmann.blogspot.com</a></p><p>Version: %1</p>").arg(version));
}

void ProfileLogger::slotAboutQt() {
  QMessageBox::aboutQt(_mainW, tr("About Qt"));
}

void ProfileLogger::slotQuitA() {
  if (getProject()) {
    if (QMessageBox::question(_mainW,
			      tr("Save?"),
			      tr("Save before closing?"),
			      QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes) == QMessageBox::Yes) {
      slotSaveProject();
    }
  }

  QApplication::quit();
}

QAction* ProfileLogger::getReloadBedsAction() {
  return _reloadBedsA;
}

QAction* ProfileLogger::getCreateBedOnTopAction() {
  return _createBedOnTopA;
}

QAction* ProfileLogger::getCreateBedAboveCurrentBedAction() {
  return _createBedAboveCurrentBedA;
}

QAction* ProfileLogger::getCreateBedBelowCurrentBedAction() {
  return _createBedBelowCurrentBedA;
}

QAction* ProfileLogger::getMoveBedUpAction() {
  return _moveBedUpA;
}

QAction* ProfileLogger::getMoveBedDownAction() {
  return _moveBedDownA;
}

QAction* ProfileLogger::getEditBedAction() {
  return _editBedA;
}

QAction* ProfileLogger::getDeleteBedAction() {
  return _deleteBedA;
}

QAction* ProfileLogger::getDuplicateBedAndInsertAtTopAction() {
  return _duplicateBedAndInsertAtTopA;
}

QAction* ProfileLogger::getSplitProfileAtBedAction() {
  return _splitProfileAtBedA;
}

QAction* ProfileLogger::getDeleteBedsAboveBedAction() {
  return _deleteBedsAboveBedA;
}

QAction* ProfileLogger::getDeleteBedsBelowBelowAction() {
  return _deleteBedsBelowBelowA;
}

QAction* ProfileLogger::getExportProfileToSvgAction() {
  return _exportProfileToSvgA;
}

QAction* ProfileLogger::getExportProfileToPdfAction() {
  return _exportProfileToPdfA;
}

QAction* ProfileLogger::getExportProfileToJpgAction() {
  return _exportProfileToJpgA;
}

QAction* ProfileLogger::getExportProfileToPngAction() {
  return _exportProfileToPngA;
}

QAction* ProfileLogger::getExportProfileToTiffAction() {
  return _exportProfileToTiffA;
}

QAction* ProfileLogger::getInsertProfileAboveBedAction() {
  return _insertProfileAboveBedA;
}

QAction* ProfileLogger::getInsertProfileBelowBedAction() {
  return _insertProfileBelowBedA;
}

ProfileItemModel* ProfileLogger::getProfileItemModel(Profile* p) {
  if (!_profileItemModels.contains(p)) {
    return 0;
  }

  return _profileItemModels.value(p);
}

BedItemModel* ProfileLogger::getBedItemModel(Bed* b) {
  if (!_bedItemModels.contains(b)) {
    return 0;
  }

  return _bedItemModels.value(b);
}

void ProfileLogger::registerProfileItemModel(Profile* p, ProfileItemModel* m) {
  _profileItemModels[p] = m;
}

void ProfileLogger::registerBedItemModel(Bed* b, BedItemModel* m) {
  _bedItemModels[b] = m;
}

void ProfileLogger::unregisterBedItemModel(Bed* b) {
  if (!_bedItemModels.contains(b)) {
    return;
  }

  _bedItemModels.remove(b);
}

void ProfileLogger::unregisterProfileItemModel(Profile* p) {
  if (!_profileItemModels.contains(p)) {
    return;
  }
  _profileItemModels.remove(p);
}

ProfileCorrelationItemModel* ProfileLogger::getProfileCorrelationItemModel() {
  return _profileCorrelationItemModel;
}

BedCorrelationItemModel* ProfileLogger::getBedCorrelationItemModel() {
  return _bedCorrelationItemModel;
}

void ProfileLogger::slotOpenDatabase()
{
  DatabaseConnectionDialog* dlg = new DatabaseConnectionDialog(getMainWindow());
  if (QDialog::Accepted != dlg->exec()) {
    return;
  }

  try {
    DatabaseConnectionSettings cs = dlg->getDatabaseConnectionSettings();
    _dbConn->open(cs);

    if (cs.getDropSchema()) {
      slotDropSchema();
    }

    if (cs.getCreateSchema()) {
      slotCreateSchema();
    }

    if (cs.getInsertTemplateData()) { 
      slotInsertTemplateData();
    }
  }
  catch(DatabaseError e) {
    DatabaseErrorDialog dlg(activeWindow(), e);
    dlg.exec();
  }
}

void ProfileLogger::slotCloseDatabase()
{
  _dbConn->close();
}

void ProfileLogger::setMainWindow(MainWindow* w) {
  _mainW = w;

  connect(_dbConn, SIGNAL(connectionEstablished(const QString&)), _mainW, SLOT(slotDatabaseConnectionEstablished(const QString&)));
  connect(_dbConn, SIGNAL(connectionLost()), _mainW, SLOT(slotDatabaseConnectionLost()));
  connect(_dbConn, SIGNAL(connectionClosed()), _mainW, SLOT(slotDatabaseConnectionClosed()));
}

QAction* ProfileLogger::getCloseDatabaseAction() {
  return _closeDatabaseA;
}

QAction* ProfileLogger::getOpenDatabaseAction() {
  return _openDatabaseA;
}

void ProfileLogger::slotQuit() {
  QApplication::quit();
}


QAction* ProfileLogger::getDropSchemaAction() {
  return _dropSchemaA;
}

QAction* ProfileLogger::getCreateSchemaAction() {
  return _createSchemaA;
}

QAction* ProfileLogger::getInsertTemplateDataAction() {
  return _insertTemplateDataA;
}

void ProfileLogger::slotDropSchema() {
  try {
    _dbConn->begin();
    _dbConn->dropSchema(_db);
    _dbConn->commit();
  }
  catch(DatabaseError e) {
    _dbConn->rollback();
    DatabaseErrorDialog dlg(activeWindow(), e);
    dlg.exec();
  }
}

void ProfileLogger::slotCreateSchema() {
  try {
    _dbConn->begin();
    _dbConn->createSchema(_db);
    _dbConn->commit();
  }
  catch(DatabaseError e) {
    _dbConn->rollback();
    DatabaseErrorDialog dlg(activeWindow(), e);
    dlg.exec();
  }
}

void ProfileLogger::slotInsertTemplateData() {
  try {
    _dbConn->begin();
    _dbConn->insertTemplateData();
    _dbConn->commit();
  }
  catch(DatabaseError e) {
    _dbConn->rollback();
    DatabaseErrorDialog dlg(activeWindow(), e);
    dlg.exec();
  }
}

