/* 
 * File:   ProfileEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _PROFILEEDITORDIALOG_H
#define	_PROFILEEDITORDIALOG_H

#include "DatasetEditorDialog.h"
#include "BedEditorDialog.h"
#include "CsvProfileImportSettingsDialog.h"
#include "MainWindow.h"

class Profile;
class LengthUnitsComboBox;

class QSpinBox;

class LengthMeasurementWidget;

class ProfileEditorDialog: public DatasetEditorDialog {
    Q_OBJECT
public:
    ProfileEditorDialog(QWidget* parent, Profile* p);
    virtual ~ProfileEditorDialog();
    Profile* getProfile();

public slots:
    void slotMaxSymbolSizeChanged(int size);
    void slotScaleChanged(int scale);
    void slotLegendColumnsChanged(int c);
    void slotCellSizeChanged(int s);
    void slotDefaultLengthUnitChanged(LengthUnit* u);

    void slotShowHeightToggled(bool toggled);
    void slotShowBedNumberToggled(bool toggled);
    void slotShowLithologyToggled(bool toggled);
    void slotShowBeddingTypeToggled(bool toggled);
    void slotShowTopBoundaryTypeToggled(bool toggled);
    void slotShowFossilsToggled(bool toggled);
    void slotShowSedimentStructuresToogled(bool toggled);
    void slotShowGrainSizeToggled(bool toggled);
    void slotShowCustomSymbolsToggled(bool toggled);
    void slotShowNotesToggled(bool toggled);
    void slotShowColorToggled(bool toggled);
    void slotShowFaciesToggled(bool toggled);
    void slotShowLithologicalUnitToggled(bool toggled);
    void slotShowOutcropQualityToggled(bool toggled);
    void slotShowHeightMarksToggled(bool toggled);
    
private:
    void setupMainPage();
    void setupPresentationPage();
    void setupVisibilityPage();
    void showData();
    
    QSpinBox* _maxSymbolSizeW;
    QSpinBox* _scaleW;
    QSpinBox* _cellSizeW;
    QSpinBox* _legendColumnsW;
    LengthMeasurementWidget* _bigMarksDistanceW;
    LengthMeasurementWidget* _smallMarksDistanceW;
    LengthUnitsComboBox* _defaultUnitW;
    
    QCheckBox* _showHeightW;
    QCheckBox* _showBedNumbersW;
    QCheckBox* _showLithologyW;
    QCheckBox* _showBeddingTypeW;
    QCheckBox* _showTopBoundaryTypeW;
    QCheckBox* _showFossilsW;
    QCheckBox* _showSedimentStructuresW;
    QCheckBox* _showGrainSizeW;
    QCheckBox* _showCustomSymbolsW;
    QCheckBox* _showNotesW;
    QCheckBox* _showColorW;
    QCheckBox* _showFaciesW;
    QCheckBox* _showLithologicalUnitW;
    QCheckBox* _showOutcropQualityW;
    QCheckBox* _showHeightMarksW;
};

#endif	/* _PROFILEEDITORDIALOG_H */

