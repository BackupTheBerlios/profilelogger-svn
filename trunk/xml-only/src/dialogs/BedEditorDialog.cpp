/* 
 * File:   BedEditorDialog.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 14:05
 */

#include "BedEditorDialog.h"

#include <QLayout>
#include <QDialogButtonBox>
#include <QLabel>
#include <QGroupBox>
#include <QApplication>
#include <QTabWidget>
#include <QWidget>
#include <QPushButton>
#include <QMessageBox>
#include <qmetatype.h>

#include "ProfileLogger.h"
#include "IdLabel.h"
#include "DescriptionEdit.h"
#include "OutcropQualityView.h"
#include "ColorView.h"
#include "LithologyView.h"
#include "BeddingTypeView.h"
#include "BoundaryTypeView.h"
#include "GrainSizeModeSelectorWidget.h"
#include "CarbonateGrainSizeView.h"
#include "ClasticGrainSizeView.h"
#include "GrainSizeModes.h"
#include "Bed.h"
#include "FossilInBedItemModel.h"
#include "FossilItemModel.h"
#include "FossilView.h"
#include "FossilInBedView.h"
#include "Fossil.h"
#include "SedimentStructureInBedItemModel.h"
#include "SedimentStructureItemModel.h"
#include "SedimentStructureView.h"
#include "SedimentStructureInBedView.h"
#include "SedimentStructure.h"
#include "CustomSymbolInBedItemModel.h"
#include "CustomSymbolItemModel.h"
#include "CustomSymbolView.h"
#include "CustomSymbolInBedView.h"
#include "CustomSymbol.h"
#include "LengthMeasurement.h"
#include "LengthMeasurementWidget.h"
#include "BedPropertyPage.h"
#include "FaciesItemModel.h"
#include "FaciesView.h"
#include "LithologicalUnitView.h"
#include "Lithology.h"

BedEditorDialog::BedEditorDialog(QWidget* parent, Bed* bed)
: QDialog(parent),
_bed(bed) {
    setLayout(new QVBoxLayout(this));
    setupGui(this);
    showData();
    setSizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::MinimumExpanding);
}

BedEditorDialog::~BedEditorDialog() {
}

void BedEditorDialog::setupButtons(QWidget* parent) {
    _bbW = new QDialogButtonBox(QDialogButtonBox::Ok, Qt::Horizontal, parent);
    parent->layout()->addWidget(_bbW);
    connect(_bbW, SIGNAL(accepted()), this, SLOT(accept()));
}

void BedEditorDialog::setupDetailsWidget(QWidget* parent) {
    _detailsW = new QTabWidget(parent);
    _detailsW->setMinimumHeight(400);
    parent->layout()->addWidget(_detailsW);

    setupOutcropQualityPage();
    setupColorPage();
    setupLithologyPage();
    setupBeddingTypePage();
    setupBoundaryTypePage();
    setupCarbonateGrainSizePage();
    setupClasticGrainSizePage();
    setupFossilsPage();
    setupSedimentStructuresPage();
    setupCustomSymbolsPage();
    setupFaciesPage();
    setupLithologicalUnitPage();

    _detailsW->addTab(_outcropQualityP, tr("Outcrop Quality"));
    _detailsW->addTab(_colorP, tr("Colors"));
    _detailsW->addTab(_lithologyP, tr("Lithologies"));
    _detailsW->addTab(_beddingTypeP, tr("Bedding"));
    _detailsW->addTab(_boundaryTypeP, tr("Top Boundary Type"));
    _detailsW->addTab(_carbonateGrainSizeP, tr("Carb Grains"));
    _detailsW->addTab(_clasticGrainSizeP, tr("Clastic Grains"));
    _detailsW->addTab(_faciesP, tr("Facies"));
    _detailsW->addTab(_lithologicalUnitP, tr("Lithological Unit"));
    _detailsW->addTab(_fossilP, tr("Fossils"));
    _detailsW->addTab(_sedimentStructureP, tr("Sed Structs"));
    _detailsW->addTab(_customSymbolP, tr("Custom Symbols"));
}

void BedEditorDialog::setupGui(QWidget* parent) {
    _mainW = new QFrame(parent);
    _mainW->setLayout(new QVBoxLayout());
    parent->layout()->addWidget(_mainW);

    setupTopBox(_mainW);
    setupDetailsWidget(_mainW);
    setupButtons(this);
}

void BedEditorDialog::setupTopBox(QWidget* parent) {
    QWidget* topW = new QWidget(parent);
    topW->setLayout(new QHBoxLayout(topW));
    parent->layout()->addWidget(topW);

    setupMainBox(topW);
    setupMainSecondaryBox(topW);
}

void BedEditorDialog::setupMainBox(QWidget* parent) {
    _mainBoxW = new QGroupBox(tr("Bed"), parent);
    _mainBoxW->setLayout(new QGridLayout(_mainBoxW));

    _idW = new IdLabel(_mainBoxW);
    _bedNumberW = new QLabel(tr("<Not Set>"), _mainBoxW);
    _descriptionW = new DescriptionEdit(_mainBoxW);
    connect(_descriptionW, SIGNAL(descriptionChanged(const QString&)), this, SLOT(slotDescriptionChanged(const QString&)));

    int r = 0;
    int wC = 1;
    int lC = 0;
    ((QGridLayout*) _mainBoxW->layout())->addWidget(_idW->getLabel(), r, lC);
    ((QGridLayout*) _mainBoxW->layout())->addWidget(_idW, r, wC);
    r++;
    ((QGridLayout*) _mainBoxW->layout())->addWidget(new QLabel(tr("Bed #"), _mainBoxW), r, lC);
    ((QGridLayout*) _mainBoxW->layout())->addWidget(_bedNumberW, r, wC);
    r++;
    ((QGridLayout*) _mainBoxW->layout())->addWidget(_descriptionW->getLabel(), r, lC);
    ((QGridLayout*) _mainBoxW->layout())->addWidget(_descriptionW, r, wC);

    parent->layout()->addWidget(_mainBoxW);
}

void BedEditorDialog::setupMainSecondaryBox(QWidget* parent) {
    QWidget* rightW = new QWidget(parent);
    parent->layout()->addWidget(rightW);
    rightW->setLayout(new QVBoxLayout(rightW));

    setupHeightWidget(rightW);
    setupGrainSizeWidget(rightW);
}

void BedEditorDialog::setupHeightWidget(QWidget* parent) {
    _heightB = new QGroupBox(tr("Height"), parent);
    _heightB->setLayout(new QHBoxLayout(_heightB));
    _heightW = new LengthMeasurementWidget(_heightB);

    _heightB->layout()->addWidget(_heightW);
    parent->layout()->addWidget(_heightB);
}

void BedEditorDialog::setupOutcropQualityPage() {
    _outcropQualityP = new QWidget(_detailsW);
    _outcropQualityP->setLayout(new QVBoxLayout(_outcropQualityP));
    _outcropQualityV = new OutcropQualityView(_outcropQualityP,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getOutcropQualityItemModel());
    _outcropQualityP->layout()->addWidget(_outcropQualityV);
    connect(_outcropQualityV, SIGNAL(currentOutcropQualityChanged(OutcropQuality*)), this, SLOT(slotOutcropQualityChanged(OutcropQuality*)));
}

void BedEditorDialog::setupGrainSizeWidget(QWidget* parent) {
    _grainSizeModesW = new GrainSizeModeSelectorWidget(parent);
    _copyGrainSizeFromLithologyW = new QPushButton(tr("Copy From Lithology"), _grainSizeModesW);
    _grainSizeModesW->layout()->addWidget(_copyGrainSizeFromLithologyW);
    connect(_grainSizeModesW, SIGNAL(modeChanged(GrainSizeModes)), this, SLOT(slotGrainSizeModeChanged(GrainSizeModes)));
    connect(_copyGrainSizeFromLithologyW, SIGNAL(clicked()), this, SLOT(slotCopyGrainSizesFromLithology()));
    _copyGrainSizeFromLithologyW->setEnabled(false);
    parent->layout()->addWidget(_grainSizeModesW);
}

void BedEditorDialog::showData() {
    if (!_bed) {
        return;
    }

    _copyGrainSizeFromLithologyW->setEnabled(_bed->hasLithology());
    
    _idW->setId(_bed->getId());
    _bedNumberW->setText(QString::number(_bed->getPosition()));
    _descriptionW->setText(_bed->getDescription());
    _heightW->setMeasurement(_bed->getHeight());

    _outcropQualityV->selectOutcropQuality(_bed->getOutcropQuality());
    _colorV->selectColor(_bed->getColor());
    _lithologyV->selectLithology(_bed->getLithology());
    _beddingTypeV->selectBeddingType(_bed->getBeddingType());
    _topBoundaryTypeV->selectBoundaryType(_bed->getTopBoundaryType());
    _faciesV->selectFacies(_bed->getFacies());

    _grainSizeModesW->setMode(_bed->getGrainSizeMode());

    _baseCarbonateGrainSizeV->selectCarbonateGrainSize(_bed->getBaseCarbonateGrainSize());
    _topCarbonateGrainSizeV->selectCarbonateGrainSize(_bed->getTopCarbonateGrainSize());
    _baseClasticGrainSizeV->selectClasticGrainSize(_bed->getBaseClasticGrainSize());
    _topClasticGrainSizeV->selectClasticGrainSize(_bed->getTopClasticGrainSize());

    _assignedFossilsM->slotCurrentBedChanged(_bed);
    _assignedFossilsV->slotCurrentBedChanged(_bed);

    _assignedSedimentStructuresM->slotCurrentBedChanged(_bed);
    _assignedSedimentStructuresV->slotCurrentBedChanged(_bed);

    _assignedCustomSymbolsM->slotCurrentBedChanged(_bed);
    _assignedCustomSymbolsV->slotCurrentBedChanged(_bed);

    _carbonateGrainSizeP->setEnabled(CarbonateGrainSizeMode == _bed->getGrainSizeMode());
    _clasticGrainSizeP->setEnabled(ClasticGrainSizeMode == _bed->getGrainSizeMode());
}

void BedEditorDialog::slotDescriptionChanged(const QString& s) {
    _bed->setDescription(s);
}

void BedEditorDialog::slotOutcropQualityChanged(OutcropQuality* o) {
    _bed->setOutcropQuality(o);
}

void BedEditorDialog::slotColorChanged(Color* c) {
    _bed->setColor(c);
}

void BedEditorDialog::slotLithologicalUnitChanged(LithologicalUnit* c) {
    _bed->setLithologicalUnit(c);
}

void BedEditorDialog::slotLithologyChanged(Lithology* c) {
    _bed->setLithology(c);
    _copyGrainSizeFromLithologyW->setEnabled(_bed->hasLithology());
}

void BedEditorDialog::slotFaciesChanged(Facies* c) {
    _bed->setFacies(c);
}

void BedEditorDialog::slotBeddingTypeChanged(BeddingType* c) {
    _bed->setBeddingType(c);
}

void BedEditorDialog::slotTopBoundaryTypeChanged(BoundaryType* c) {
    _bed->setTopBoundaryType(c);
}

void BedEditorDialog::slotGrainSizeModeChanged(GrainSizeModes m) {
    _bed->setGrainSizeMode(m);

    if (_bed->getGrainSizeMode() == CarbonateGrainSizeMode) {
        _carbonateGrainSizeP->setEnabled(true);
        _clasticGrainSizeP->setEnabled(false);
    }
    if (_bed->getGrainSizeMode() == ClasticGrainSizeMode) {
        _carbonateGrainSizeP->setEnabled(false);
        _clasticGrainSizeP->setEnabled(true);
    }
}

void BedEditorDialog::slotBaseCarbonateGrainSizeChanged(CarbonateGrainSize* s) {
    _bed->setBaseCarbonateGrainSize(s);
}

void BedEditorDialog::slotTopCarbonateGrainSizeChanged(CarbonateGrainSize* s) {
    _bed->setTopCarbonateGrainSize(s);
}

void BedEditorDialog::slotBaseClasticGrainSizeChanged(ClasticGrainSize* s) {
    _bed->setBaseClasticGrainSize(s);
}

void BedEditorDialog::slotTopClasticGrainSizeChanged(ClasticGrainSize* s) {
    _bed->setTopClasticGrainSize(s);
}

void BedEditorDialog::slotAddFossils() {
    _bed->addFossils(_availableFossilsV->getSelectedFossils());
    _assignedFossilsM->reload();
}

void BedEditorDialog::slotRemoveFossils() {
    _bed->removeFossils(_assignedFossilsV->getSelectedFossils());
    _assignedFossilsM->reload();
}

void BedEditorDialog::slotAddSedimentStructures() {
    _bed->addSedimentStructures(_availableSedimentStructuresV->getSelectedSedimentStructures());
    _assignedSedimentStructuresM->reload();
}

void BedEditorDialog::slotRemoveSedimentStructures() {
    _bed->removeSedimentStructures(_assignedSedimentStructuresV->getSelectedSedimentStructures());
    _assignedSedimentStructuresM->reload();
}

void BedEditorDialog::slotAddCustomSymbols() {
    _bed->addCustomSymbols(_availableCustomSymbolsV->getSelectedCustomSymbols());
    _assignedCustomSymbolsM->reload();
}

void BedEditorDialog::slotRemoveCustomSymbols() {
    _bed->removeCustomSymbols(_assignedCustomSymbolsV->getSelectedCustomSymbols());
    _assignedCustomSymbolsM->reload();
}

void BedEditorDialog::setupColorPage() {
    _colorP = new BedPropertyPage(_detailsW);
    _colorV = new ColorView(_colorP, (static_cast<ProfileLogger*> (QApplication::instance()))->getColorItemModel());

    _colorP->addWidgets(tr("Color"), _colorV);

    connect(_colorV, SIGNAL(currentColorChanged(Color*)), this, SLOT(slotColorChanged(Color*)));
}

void BedEditorDialog::setupLithologicalUnitPage() {
    _lithologicalUnitP = new BedPropertyPage(_detailsW);
    _lithologicalUnitV = new LithologicalUnitView(_lithologicalUnitP, (static_cast<ProfileLogger*> (QApplication::instance()))->getLithologicalUnitItemModel());

    _lithologicalUnitP->addWidgets(tr("Lithological Unit"), _lithologicalUnitV);

    connect(_lithologicalUnitV, SIGNAL(currentLithologicalUnitChanged(LithologicalUnit*)), this, SLOT(slotLithologicalUnitChanged(LithologicalUnit*)));
}

void BedEditorDialog::setupLithologyPage() {
    _lithologyP = new BedPropertyPage(_detailsW);
    _lithologyV = new LithologyView(_lithologyP, (static_cast<ProfileLogger*> (QApplication::instance()))->getLithologyItemModel());

    _lithologyP->addWidgets(tr("Lithology"), _lithologyV);

    connect(_lithologyV, SIGNAL(currentLithologyChanged(Lithology*)), this, SLOT(slotLithologyChanged(Lithology*)));
}

void BedEditorDialog::setupFaciesPage() {
    _faciesP = new BedPropertyPage(_detailsW);
    _faciesV = new FaciesView(_faciesP, (static_cast<ProfileLogger*> (QApplication::instance()))->getFaciesItemModel());

    _faciesP->addWidgets(tr("Facies"), _faciesV);

    connect(_faciesV, SIGNAL(currentFaciesChanged(Facies*)), this, SLOT(slotFaciesChanged(Facies*)));
}

void BedEditorDialog::setupBeddingTypePage() {
    _beddingTypeP = new BedPropertyPage(_detailsW);
    _beddingTypeV = new BeddingTypeView(_beddingTypeP, (static_cast<ProfileLogger*> (QApplication::instance()))->getBeddingTypeItemModel());

    _beddingTypeP->addWidgets(tr("Bedding Type"), _beddingTypeV);

    connect(_beddingTypeV, SIGNAL(currentBeddingTypeChanged(BeddingType*)), this, SLOT(slotBeddingTypeChanged(BeddingType*)));
}

void BedEditorDialog::setupBoundaryTypePage() {
    _boundaryTypeP = new BedPropertyPage(_detailsW);
    _topBoundaryTypeV = new BoundaryTypeView(_boundaryTypeP, (static_cast<ProfileLogger*> (QApplication::instance()))->getBoundaryTypeItemModel());

    _boundaryTypeP->addWidgets(tr("Top Boundary Type"), _topBoundaryTypeV);

    connect(_topBoundaryTypeV, SIGNAL(currentBoundaryTypeChanged(BoundaryType*)), this, SLOT(slotTopBoundaryTypeChanged(BoundaryType*)));
}

void BedEditorDialog::setupClasticGrainSizePage() {
    _clasticGrainSizeP = new BedPropertyPage(_detailsW);
    _baseClasticGrainSizeV = new ClasticGrainSizeView(_clasticGrainSizeP,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getClasticGrainSizeItemModel());
    _topClasticGrainSizeV = new ClasticGrainSizeView(_clasticGrainSizeP,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getClasticGrainSizeItemModel());

    _clasticGrainSizeP->addWidgets(tr("Base Clastic Grain Size"), tr("Top Clastic Grain Size"),
            _baseClasticGrainSizeV, _topClasticGrainSizeV);

    connect(_topClasticGrainSizeV, SIGNAL(currentClasticGrainSizeChanged(ClasticGrainSize*)), this, SLOT(slotTopClasticGrainSizeChanged(ClasticGrainSize*)));
    connect(_baseClasticGrainSizeV, SIGNAL(currentClasticGrainSizeChanged(ClasticGrainSize*)), this, SLOT(slotBaseClasticGrainSizeChanged(ClasticGrainSize*)));
}

void BedEditorDialog::setupCarbonateGrainSizePage() {
    _carbonateGrainSizeP = new BedPropertyPage(_detailsW);
    _baseCarbonateGrainSizeV = new CarbonateGrainSizeView(_carbonateGrainSizeP,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getCarbonateGrainSizeItemModel());
    _topCarbonateGrainSizeV = new CarbonateGrainSizeView(_carbonateGrainSizeP,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getCarbonateGrainSizeItemModel());

    _carbonateGrainSizeP->addWidgets(tr("Base Carbonate Grain Size"), tr("Top Carbonate Grain Size"),
            _baseCarbonateGrainSizeV, _topCarbonateGrainSizeV);

    connect(_topCarbonateGrainSizeV, SIGNAL(currentCarbonateGrainSizeChanged(CarbonateGrainSize*)), this, SLOT(slotTopCarbonateGrainSizeChanged(CarbonateGrainSize*)));
    connect(_baseCarbonateGrainSizeV, SIGNAL(currentCarbonateGrainSizeChanged(CarbonateGrainSize*)), this, SLOT(slotBaseCarbonateGrainSizeChanged(CarbonateGrainSize*)));
}

void BedEditorDialog::setupFossilsPage() {
    _fossilP = new BedPropertyPage(_detailsW);

    _assignedFossilsM = new FossilInBedItemModel(this);
    _availableFossilsV = new FossilView(_detailsW, (static_cast<ProfileLogger*> (QApplication::instance()))->getFossilItemModel());
    _assignedFossilsV = new FossilInBedView(_detailsW, _assignedFossilsM);

    QWidget* fossilActionsW = new QWidget(_fossilP);
    fossilActionsW->setLayout(new QVBoxLayout(fossilActionsW));
    _addFossilsW = new QPushButton(tr("Add >"), fossilActionsW);
    _removeFossilsW = new QPushButton(tr("< Remove"), fossilActionsW);

    fossilActionsW->layout()->addWidget(_addFossilsW);
    fossilActionsW->layout()->addWidget(_removeFossilsW);

    _fossilP->addWidgets(tr("Available Fossils"), tr("Fossils In Bed"),
            _availableFossilsV, _assignedFossilsV, fossilActionsW);

    connect(_addFossilsW, SIGNAL(clicked()), this, SLOT(slotAddFossils()));
    connect(_removeFossilsW, SIGNAL(clicked()), this, SLOT(slotRemoveFossils()));
}

void BedEditorDialog::setupSedimentStructuresPage() {
    _sedimentStructureP = new BedPropertyPage(_detailsW);

    _assignedSedimentStructuresM = new SedimentStructureInBedItemModel(this);
    _availableSedimentStructuresV = new SedimentStructureView(_detailsW,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getSedimentStructureItemModel());
    _assignedSedimentStructuresV = new SedimentStructureInBedView(_detailsW, _assignedSedimentStructuresM);

    QWidget* sedimentStructureActionsW = new QWidget(_sedimentStructureP);
    sedimentStructureActionsW->setLayout(new QVBoxLayout(sedimentStructureActionsW));
    _addSedimentStructuresW = new QPushButton(tr("Add >"), sedimentStructureActionsW);
    _removeSedimentStructuresW = new QPushButton(tr("< Remove"), sedimentStructureActionsW);

    sedimentStructureActionsW->layout()->addWidget(_addSedimentStructuresW);
    sedimentStructureActionsW->layout()->addWidget(_removeSedimentStructuresW);

    _sedimentStructureP->addWidgets(tr("Available Sediment Structures"), tr("Sediment Structures In Bed"),
            _availableSedimentStructuresV, _assignedSedimentStructuresV, sedimentStructureActionsW);

    connect(_addSedimentStructuresW, SIGNAL(clicked()), this, SLOT(slotAddSedimentStructures()));
    connect(_removeSedimentStructuresW, SIGNAL(clicked()), this, SLOT(slotRemoveSedimentStructures()));
}

void BedEditorDialog::setupCustomSymbolsPage() {
    _customSymbolP = new BedPropertyPage(_detailsW);

    _assignedCustomSymbolsM = new CustomSymbolInBedItemModel(this);
    _availableCustomSymbolsV = new CustomSymbolView(_detailsW, (static_cast<ProfileLogger*> (QApplication::instance()))->getCustomSymbolItemModel());
    _assignedCustomSymbolsV = new CustomSymbolInBedView(_detailsW, _assignedCustomSymbolsM);

    QWidget* customSymbolActionsW = new QWidget(_customSymbolP);
    customSymbolActionsW->setLayout(new QVBoxLayout(customSymbolActionsW));
    _addCustomSymbolsW = new QPushButton(tr("Add >"), customSymbolActionsW);
    _removeCustomSymbolsW = new QPushButton(tr("< Remove"), customSymbolActionsW);

    customSymbolActionsW->layout()->addWidget(_addCustomSymbolsW);
    customSymbolActionsW->layout()->addWidget(_removeCustomSymbolsW);

    _customSymbolP->addWidgets(tr("Available Custom Symbols"), tr("Custom Symbols In Bed"),
            _availableCustomSymbolsV, _assignedCustomSymbolsV, customSymbolActionsW);

    connect(_addCustomSymbolsW, SIGNAL(clicked()), this, SLOT(slotAddCustomSymbols()));
    connect(_removeCustomSymbolsW, SIGNAL(clicked()), this, SLOT(slotRemoveCustomSymbols()));
}

void BedEditorDialog::accept() {
    if (!_bed->hasValidHeight()) {
        QMessageBox::information(this,
                tr("Bed Not Valid"),
                tr("Cowardly refusing to create bed with invalid height."));
        return;
    }

    done(QDialog::Accepted);
}

void BedEditorDialog::reject() {
    // ignore
}

void BedEditorDialog::slotCopyGrainSizesFromLithology() {
    if (!_bed->hasLithology()) {
        QMessageBox::information(this, tr("Select Lithology First"), tr("Select Lithology First."));
        return;
    }

    if (QMessageBox::Yes != QMessageBox::question(this,
            tr("Copy Grain Size Data"),
            tr("<p>Set default grain size mode to <b>%1</b> and base and top grain sizes to <b>%2</b>?<p><p>Previously entered grain size data will be overwritten.</p>")
            .arg(_bed->getLithology()->getDefaultGrainSizeModeName())
            .arg(_bed->getLithology()->getDefaultGrainSizeName()),
            QMessageBox::Yes | QMessageBox::No)) {
        return;
    }

    Lithology* l = _bed->getLithology();

    _grainSizeModesW->setMode(l->getDefaultGrainSizeMode());

    QApplication::processEvents();
    
    switch(l->getDefaultGrainSizeMode()) {
        case(CarbonateGrainSizeMode): {
            _bed->setBaseCarbonateGrainSize(l->getDefaultCarbonateGrainSize());
            _bed->setTopCarbonateGrainSize(l->getDefaultCarbonateGrainSize());

            _baseCarbonateGrainSizeV->selectCarbonateGrainSize(_bed->getBaseCarbonateGrainSize());
            _topCarbonateGrainSizeV->selectCarbonateGrainSize(_bed->getTopCarbonateGrainSize());
            break;
        }
        case(ClasticGrainSizeMode): {
            _bed->setBaseClasticGrainSize(l->getDefaultClasticGrainSize());
            _bed->setTopClasticGrainSize(l->getDefaultClasticGrainSize());

            _baseClasticGrainSizeV->selectClasticGrainSize(_bed->getBaseClasticGrainSize());
            _topClasticGrainSizeV->selectClasticGrainSize(_bed->getTopClasticGrainSize());
            break;
        }
    }
}
