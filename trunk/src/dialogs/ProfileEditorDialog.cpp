/* 
 * File:   ProfileEditorDialog.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 21:39
 */

#include "ProfileEditorDialog.h"

#include <QSpinBox>
#include <QGroupBox>
#include <QLayout>
#include <QCheckBox>

#include "LengthMeasurementWidget.h"
#include "LengthUnitsComboBox.h"

#include "Profile.h"

ProfileEditorDialog::ProfileEditorDialog(QWidget* parent, Profile* p)
: DatasetEditorDialog(parent, p) {
    setupMainPage();
    setupPresentationPage();
    setupVisibilityPage();

    emit showDatasetRequest(getProfile());
    slotShowDataset(getProfile());
    showData();
}

void ProfileEditorDialog::showData() {
    _defaultUnitW->setLengthUnit(getProfile()->getDefaultUnit());
    _scaleW->setValue(getProfile()->getScale());

    _cellSizeW->setValue(getProfile()->getCellSize());
    _legendColumnsW->setValue(getProfile()->getLegendColumns());
    _bigMarksDistanceW->setMeasurement(getProfile()->getBigMarksDistance());
    _smallMarksDistanceW->setMeasurement(getProfile()->getSmallMarksDistance());
    _maxSymbolSizeW->setValue(getProfile()->getMaxSymbolSize());

    _showHeightW->setChecked(getProfile()->getShowHeight());
    _showBedNumbersW->setChecked(getProfile()->getShowBedNumbers());
    _showLithologyW->setChecked(getProfile()->getShowLithology());
    _showBeddingTypeW->setChecked(getProfile()->getShowBeddingType());
    _showTopBoundaryTypeW->setChecked(getProfile()->getShowTopBoundaryType());
    _showFossilsW->setChecked(getProfile()->getShowFossils());
    _showSedimentStructuresW->setChecked(getProfile()->getShowSedimentStructures());
    _showGrainSizeW->setChecked(getProfile()->getShowGrainSize());
    _showCustomSymbolsW->setChecked(getProfile()->getShowCustomSymbols());
    _showNotesW->setChecked(getProfile()->getShowNotes());
    _showColorW->setChecked(getProfile()->getShowColor());
    _showFaciesW->setChecked(getProfile()->getShowFacies());
    _showLithologicalUnitW->setChecked(getProfile()->getShowLithologicalUnit());
    _showOutcropQualityW->setChecked(getProfile()->getShowOutcropQuality());
    _showHeightMarksW->setChecked(getProfile()->getShowHeightMarks());

    if (!getProfile()->getShowGrainSize()) {
        _showBeddingTypeW->setChecked(false);
        _showBeddingTypeW->setEnabled(false);
        getProfile()->setShowBeddingType(false);
    } else {
        _showBeddingTypeW->setEnabled(true);
    }
}

void ProfileEditorDialog::setupPresentationPage() {
    QWidget* w = new QWidget(getTabWidget());
    QGridLayout* l = new QGridLayout(w);

    int llC = 0;
    int lwC = 1;
    int lr = 0;

    _cellSizeW = new QSpinBox(w);
    _cellSizeW->setRange(5, 100);
    _cellSizeW->setToolTip(tr("This defines how much one unit of the scaled measurement is on paper. i.e. one unit should be one cm in most cases."));

    _legendColumnsW = new QSpinBox(w);
    _legendColumnsW->setRange(1, 30);
    _legendColumnsW->setToolTip(tr("This defines how many columns there are in the legend view."));

    _bigMarksDistanceW = new LengthMeasurementWidget(w);
    _bigMarksDistanceW->setToolTip(tr("This defines on which distance marks should be drawn outside the column view."));
    _smallMarksDistanceW = new LengthMeasurementWidget(getMainPage());
    _smallMarksDistanceW->setToolTip(tr("This is the distance small marks should be drawn inside of the column view."));

    _maxSymbolSizeW = new QSpinBox(w);
    _maxSymbolSizeW->setRange(10, 500);
    _maxSymbolSizeW->setToolTip(tr("This defines the maximum height and width of symbols (fossils, sediment structures, custom symbols)."));

    l->addWidget(new QLabel(tr("Max Symbol Size"), getMainPage()), lr, llC);
    l->addWidget(_maxSymbolSizeW, lr, lwC);
    lr++;

    l->addWidget(new QLabel(tr("Columns in Legend"), getMainPage()), lr, llC);
    l->addWidget(_legendColumnsW, lr, lwC);
    lr++;

    l->addWidget(new QLabel(tr("Profile Cell Size:"), getMainPage()), lr, llC);
    l->addWidget(_cellSizeW, lr, lwC);
    lr++;

    l->addWidget(new QLabel(tr("Big Marks Distance"), getMainPage()), lr, llC);
    l->addWidget(_bigMarksDistanceW, lr, lwC);
    lr++;

    l->addWidget(new QLabel(tr("Small Marks Distance"), getMainPage()), lr, llC);
    l->addWidget(_smallMarksDistanceW, lr, lwC);
    lr++;

    connect(_maxSymbolSizeW, SIGNAL(valueChanged(int)), this, SLOT(slotMaxSymbolSizeChanged(int)));
    connect(_cellSizeW, SIGNAL(valueChanged(int)), this, SLOT(slotCellSizeChanged(int)));
    connect(_legendColumnsW, SIGNAL(valueChanged(int)), this, SLOT(slotLegendColumnsChanged(int)));

    getTabWidget()->addTab(w, tr("Presentation"));
}

void ProfileEditorDialog::setupVisibilityPage() {
    QWidget* w = new QWidget(getTabWidget());
    QBoxLayout* l = new QVBoxLayout(w);

    _showHeightW = new QCheckBox(tr("Show Height"), w);
    _showBedNumbersW = new QCheckBox(tr("Show Bed Numbers"), w);
    _showLithologyW = new QCheckBox(tr("Show Lithology"), w);
    _showBeddingTypeW = new QCheckBox(tr("Show Bedding Type"), w);
    _showTopBoundaryTypeW = new QCheckBox(tr("Show Top Boundary Type"), w);
    _showFossilsW = new QCheckBox(tr("Show Fossils"), w);
    _showSedimentStructuresW = new QCheckBox(tr("Show Sedimente Structures"), w);
    _showGrainSizeW = new QCheckBox(tr("Show Grain Size"), w);
    _showCustomSymbolsW = new QCheckBox(tr("Show Custom Symbols"), w);
    _showNotesW = new QCheckBox(tr("Show Notes"), w);
    _showColorW = new QCheckBox(tr("Show Color"), w);
    _showFaciesW = new QCheckBox(tr("Show Facies"), w);
    _showLithologicalUnitW = new QCheckBox(tr("Show Lithological Unit"), w);
    _showOutcropQualityW = new QCheckBox(tr("Show Outcrop Quality"), w);
    _showHeightMarksW = new QCheckBox(tr("Show Height Marks"), w);

    l->addWidget(_showHeightW);
    l->addWidget(_showBedNumbersW);
    l->addWidget(_showLithologyW);
    l->addWidget(_showBeddingTypeW);
    l->addWidget(_showTopBoundaryTypeW);
    l->addWidget(_showColorW);
    l->addWidget(_showFaciesW);
    l->addWidget(_showHeightW);
    l->addWidget(_showLithologicalUnitW);
    l->addWidget(_showOutcropQualityW);
    l->addWidget(_showHeightMarksW);
    l->addWidget(_showFossilsW);
    l->addWidget(_showSedimentStructuresW);
    l->addWidget(_showGrainSizeW);
    l->addWidget(_showCustomSymbolsW);
    l->addWidget(_showNotesW);

    connect(_showBedNumbersW, SIGNAL(toggled(bool)), this, SLOT(slotShowBedNumbersToggled(bool)));
    connect(_showHeightW, SIGNAL(toggled(bool)), this, SLOT(slotShowHeightToggled(bool)));
    connect(_showLithologyW, SIGNAL(toggled(bool)), this, SLOT(slotShowLithologyToggled(bool)));
    connect(_showBeddingTypeW, SIGNAL(toggled(bool)), this, SLOT(slotShowBeddingTypeToggled(bool)));
    connect(_showTopBoundaryTypeW, SIGNAL(toggled(bool)), this, SLOT(slotShowTopBoundaryTypeToggled(bool)));
    connect(_showFossilsW, SIGNAL(toggled(bool)), this, SLOT(slotShowFossilsToggled(bool)));
    connect(_showSedimentStructuresW, SIGNAL(toggled(bool)), this, SLOT(slotShowSedimentStructuresToogled(bool)));
    connect(_showGrainSizeW, SIGNAL(toggled(bool)), this, SLOT(slotShowGrainSizeToggled(bool)));
    connect(_showCustomSymbolsW, SIGNAL(toggled(bool)), this, SLOT(slotShowCustomSymbolsToggled(bool)));
    connect(_showNotesW, SIGNAL(toggled(bool)), this, SLOT(slotShowNotesToggled(bool)));
    connect(_showColorW, SIGNAL(toggled(bool)), this, SLOT(slotShowColorToggled(bool)));
    connect(_showFaciesW, SIGNAL(toggled(bool)), this, SLOT(slotShowFaciesToggled(bool)));
    connect(_showLithologicalUnitW, SIGNAL(toggled(bool)), this, SLOT(slotShowLithologicalUnitToggled(bool)));
    connect(_showOutcropQualityW, SIGNAL(toggled(bool)), this, SLOT(slotShowOutcropQualityToggled(bool)));
    connect(_showHeightMarksW, SIGNAL(toggled(bool)), this, SLOT(slotShowHeightMarksToggled(bool)));

    getTabWidget()->addTab(w, tr("Columns"));
}

void ProfileEditorDialog::setupMainPage() {
    addMainPage(tr("Profile"));
    addIdLabel();
    addNameEdit();

    _defaultUnitW = new LengthUnitsComboBox(getMainPage());
    
    _scaleW = new QSpinBox(getMainPage());
    _scaleW->setRange(1, 10000);
    _scaleW->setToolTip(tr("This is the classic column scale expressed in the form 1:xxx."));

    ((QGridLayout*) (getMainPage()->layout()))->addWidget(new QLabel(tr("Default Length Unit:"), getMainPage()), r, lC);
    ((QGridLayout*) (getMainPage()->layout()))->addWidget(_defaultUnitW, r, wC);
    r++;
    
    ((QGridLayout*) (getMainPage()->layout()))->addWidget(new QLabel(tr("Scale 1:"), getMainPage()), r, lC);
    ((QGridLayout*) (getMainPage()->layout()))->addWidget(_scaleW, r, wC);
    r++;

    addDescriptionEdit();
    addButtons();

    connect(_scaleW, SIGNAL(valueChanged(int)), this, SLOT(slotScaleChanged(int)));
    connect(_defaultUnitW, SIGNAL(lengthUnitChanged(LengthUnit*)), this, SLOT(slotDefaultLengthUnitChanged(LengthUnit*)));
}

ProfileEditorDialog::~ProfileEditorDialog() {
}

Profile* ProfileEditorDialog::getProfile() {
    return (Profile*) getDataset();
}

void ProfileEditorDialog::slotMaxSymbolSizeChanged(int size) {
    getProfile()->setMaxSymbolSize(size);
}

void ProfileEditorDialog::slotScaleChanged(int scale) {
    getProfile()->setScale(scale);
}

void ProfileEditorDialog::slotCellSizeChanged(int cellSize) {
    getProfile()->setCellSize(cellSize);
}

void ProfileEditorDialog::slotLegendColumnsChanged(int c) {
    getProfile()->setLegendColumns(c);
}

void ProfileEditorDialog::slotShowHeightToggled(bool toggled) {
    getProfile()->setShowHeight(toggled);
}

void ProfileEditorDialog::slotShowBedNumbersToggled(bool toggled) {
    getProfile()->setShowBedNumbers(toggled);
}

void ProfileEditorDialog::slotShowLithologyToggled(bool toggled) {
    getProfile()->setShowLithology(toggled);
}

void ProfileEditorDialog::slotShowBeddingTypeToggled(bool toggled) {
    getProfile()->setShowBeddingType(toggled);
}

void ProfileEditorDialog::slotShowTopBoundaryTypeToggled(bool toggled) {
    getProfile()->setShowTopBoundaryType(toggled);
}

void ProfileEditorDialog::slotShowFossilsToggled(bool toggled) {
    getProfile()->setShowFossils(toggled);
}

void ProfileEditorDialog::slotShowSedimentStructuresToogled(bool toggled) {
    getProfile()->setShowSedimentStructures(toggled);
}

void ProfileEditorDialog::slotShowGrainSizeToggled(bool toggled) {
    getProfile()->setShowGrainSize(toggled);

    if (!getProfile()->getShowGrainSize()) {
        _showBeddingTypeW->setChecked(false);
        _showBeddingTypeW->setEnabled(false);
        getProfile()->setShowBeddingType(false);
    } else {
        _showBeddingTypeW->setEnabled(true);
    }
}

void ProfileEditorDialog::slotShowCustomSymbolsToggled(bool toggled) {
    getProfile()->setShowCustomSymbols(toggled);
}

void ProfileEditorDialog::slotShowNotesToggled(bool toggled) {
    getProfile()->setShowNotes(toggled);
}

void ProfileEditorDialog::slotShowColorToggled(bool toggled) {
    getProfile()->setShowColor(toggled);
}

void ProfileEditorDialog::slotShowFaciesToggled(bool toggled) {
    getProfile()->setShowFacies(toggled);
}

void ProfileEditorDialog::slotShowLithologicalUnitToggled(bool toggled) {
    getProfile()->setShowLithologicalUnit(toggled);
}

void ProfileEditorDialog::slotShowOutcropQualityToggled(bool toggled) {
    getProfile()->setShowOutcropQuality(toggled);
}

void ProfileEditorDialog::slotShowHeightMarksToggled(bool toggled) {
    getProfile()->setShowHeightMarks(toggled);
}

void ProfileEditorDialog::slotDefaultLengthUnitChanged(LengthUnit* u) {
    getProfile()->setDefaultUnit(u);
}
