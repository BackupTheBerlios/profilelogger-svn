/* 
 * File:   ProfileLogger.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 19:32
 */

#ifndef _PROFILELOGGER_H
#define	_PROFILELOGGER_H

#include <QApplication>

#include <QBrush>
#include <QPixmap>
#include <QMap>

#include "CarbonateGrainSizeItem.h"
#include "ClasticGrainSizeView.h"
#include "Project.h"

class QAction;
class QGraphicsScene;
class QTranslator;

class MainWindow;
class ProfileLoggerDatabase;
class XMLInterface;
class DatabaseConnection;
class Project;
class ProfileItemModel;
class BedItemModel;
class OutcropQualityItemModel;
class ColorItemModel;
class LithologyItemModel;
class BeddingTypeItemModel;
class BoundaryTypeItemModel;
class CarbonateGrainSizeItemModel;
class ClasticGrainSizeItemModel;
class FossilItemModel;
class SedimentStructureItemModel;
class CustomSymbolItemModel;
class FaciesItemModel;
class LithologicalUnitTypeItemModel;
class LithologicalUnitItemModel;
class SampleItemModel;
class ImageItemModel;
class ProfileCorrelationItemModel;
class BedCorrelationItemModel;

class Settings;

class ProfileLogger : public QApplication {
    Q_OBJECT
public:
    ProfileLogger(int & argc, char** argv);
    virtual ~ProfileLogger();

    QAction* getOpenLastProjectAction() {
        return _openLastProjectA;
    }

    QAction* getNewProjectAction() {
        return _newProjectA;
    }

    QAction* getSaveProjectAction() {
        return _saveProjectA;
    }

    QAction* getSaveProjectAsAction() {
        return _saveProjectAsA;
    }

    QAction* getOpenProjectAction() {
        return _openProjectA;
    }

    QAction* getSettingsAction() {
        return _settingsA;
    }

    QAction* getAboutAction() {
        return _aboutA;
    }

    QAction* getAboutQtAction() {
        return _aboutQtA;
    }

    QAction* getQuitAction() {
        return _quitA;
    }

    QAction* getReloadBedsAction();
    QAction* getCreateBedOnTopAction();
    QAction* getCreateBedAboveCurrentBedAction();
    QAction* getCreateBedBelowCurrentBedAction();
    QAction* getMoveBedUpAction();
    QAction* getMoveBedDownAction();
    QAction* getEditBedAction();
    QAction* getDeleteBedAction();
    QAction* getDuplicateBedAndInsertAtTopAction();
    QAction* getSplitProfileAtBedAction();
    QAction* getInsertProfileBelowBedAction();
    QAction* getInsertProfileAboveBedAction();
    QAction* getDeleteBedsAboveBedAction();
    QAction* getDeleteBedsBelowBelowAction();
    QAction* getOpenDatabaseAction();
    QAction* getCloseDatabaseAction();

    QAction* getExportProfileToSvgAction();
    QAction* getExportProfileToPdfAction();
    QAction* getExportProfileToJpgAction();
    QAction* getExportProfileToPngAction();
    QAction* getExportProfileToTiffAction();

    ProfileItemModel* getProfileItemModel() {
        return _profileItemModel;
    }

    BedItemModel* getBedItemModel() {
        return _bedItemModel;
    }

    OutcropQualityItemModel* getOutcropQualityItemModel() {
        return _outcropQualityItemModel;
    }

    ColorItemModel* getColorItemModel() {
        return _colorItemModel;
    }

    LithologyItemModel* getLithologyItemModel() {
        return _lithologyItemModel;
    }

    FaciesItemModel* getFaciesItemModel() {
        return _faciesItemModel;
    }

    LithologicalUnitTypeItemModel* getLithologicalUnitTypeItemModel() {
        return _lithologicalUnitTypeItemModel;
    }

    LithologicalUnitItemModel* getLithologicalUnitItemModel() {
        return _lithologicalUnitItemModel;
    }

    SampleItemModel* getSampleItemModel() {
        return _sampleItemModel;
    }

    ImageItemModel* getImageItemModel() {
        return _imageItemModel;
    }

    BeddingTypeItemModel* getBeddingTypeItemModel() {
        return _beddingTypeItemModel;
    }

    BoundaryTypeItemModel* getBoundaryTypeItemModel() {
        return _boundaryTypeItemModel;
    }

    CarbonateGrainSizeItemModel* getCarbonateGrainSizeItemModel() {
        return _carbonateGrainSizeItemModel;
    }

    ClasticGrainSizeItemModel* getClasticGrainSizeItemModel() {
        return _clasticGrainSizeItemModel;
    }

    FossilItemModel* getFossilItemModel() {
        return _fossilItemModel;
    }

    SedimentStructureItemModel* getSedimentStructureItemModel() {
        return _sedimentStructureItemModel;
    }

    CustomSymbolItemModel* getCustomSymbolItemModel() {
        return _customSymbolItemModel;
    }

    Project* getProject() {
        return &_project;
    }

    Settings* getSettings() const {
        return _settings;
    }

    QBrush getBrushFromFileName(const QString& dir, const QString& fn);
    QPixmap getPixmapFromFileName(const QString& dir, const QString& fn);

    void setMainWindow(MainWindow* w);

    MainWindow* getMainWindow() {
        return _mainW;
    }

    void loadTranslation();

    ProfileItemModel* getProfileItemModel(Profile* p);
    BedItemModel* getBedItemModel(Bed* b);
    ProfileCorrelationItemModel* getProfileCorrelationItemModel();
    BedCorrelationItemModel* getBedCorrelationItemModel();

    ProfileLoggerDatabase* getProfileLoggerDatabase() const {
      return _db;
    }

    DatabaseConnection* getDatabaseConnection() const {
      return _dbConn;
    }

signals:
    void currentProjectChanged(Project* p);

public slots:
    void slotQuit();
    void slotNewProject();
    void slotSaveProject();
    void slotSaveProjectAs();
    void slotOpenProject();
    void slotManageSettings();
    void slotOpenLastProject();
    void slotAbout();
    void slotAboutQt();
    void slotQuitA();
    void registerBedItemModel(Bed* b, BedItemModel* m);
    void registerProfileItemModel(Profile* b, ProfileItemModel* m);
    void unregisterBedItemModel(Bed* b);
    void unregisterProfileItemModel(Profile* p);
    void slotOpenDatabase();
    void slotCloseDatabase();

private:
    void loadTranslation(const QString& fileName);
    void openProject(const QString& path);
    void setupModels();
    void setupActions();

    Settings* _settings;
    XMLInterface* _xif;
    Project _project;
    QTranslator* _translator;

    ProfileItemModel* _profileItemModel;
    BedItemModel* _bedItemModel;
    OutcropQualityItemModel* _outcropQualityItemModel;
    ColorItemModel* _colorItemModel;
    LithologyItemModel* _lithologyItemModel;
    BeddingTypeItemModel* _beddingTypeItemModel;
    BoundaryTypeItemModel* _boundaryTypeItemModel;
    CarbonateGrainSizeItemModel* _carbonateGrainSizeItemModel;
    ClasticGrainSizeItemModel* _clasticGrainSizeItemModel;
    FossilItemModel* _fossilItemModel;
    SedimentStructureItemModel* _sedimentStructureItemModel;
    CustomSymbolItemModel* _customSymbolItemModel;
    FaciesItemModel* _faciesItemModel;
    LithologicalUnitTypeItemModel* _lithologicalUnitTypeItemModel;
    LithologicalUnitItemModel* _lithologicalUnitItemModel;
    SampleItemModel* _sampleItemModel;
    ImageItemModel* _imageItemModel;
    ProfileCorrelationItemModel* _profileCorrelationItemModel;
    BedCorrelationItemModel* _bedCorrelationItemModel;

    QMap<Profile*, ProfileItemModel*> _profileItemModels;
    QMap<Bed*, BedItemModel*> _bedItemModels;

    QAction* _openLastProjectA;
    QAction* _openProjectA;
    QAction* _newProjectA;
    QAction* _saveProjectA;
    QAction* _saveProjectAsA;
    QAction* _settingsA;
    QAction* _aboutA;
    QAction* _aboutQtA;
    QAction* _quitA;
    QAction* _openDatabaseA;
    QAction* _closeDatabaseA;
    QAction* _reloadBedsA;
    QAction* _createBedOnTopA;
    QAction* _createBedAboveCurrentBedA;
    QAction* _createBedBelowCurrentBedA;
    QAction* _moveBedUpA;
    QAction* _moveBedDownA;
    QAction* _editBedA;
    QAction* _deleteBedA;
    QAction* _duplicateBedAndInsertAtTopA;
    QAction* _splitProfileAtBedA;
    QAction* _deleteBedsAboveBedA;
    QAction* _deleteBedsBelowBelowA;
    QAction* _insertProfileAboveBedA;
    QAction* _insertProfileBelowBedA;
    QAction* _exportProfileToSvgA;
    QAction* _exportProfileToPdfA;
    QAction* _exportProfileToJpgA;
    QAction* _exportProfileToPngA;
    QAction* _exportProfileToTiffA;

    // key: file name as in Lithology
    QMap<QString, QBrush> _brushes;
    QMap<QString, QPixmap> _pixmaps;

    MainWindow* _mainW;

    ProfileLoggerDatabase* _db;
    DatabaseConnection* _dbConn;
};

#endif	/* _PROFILELOGGER_H */

