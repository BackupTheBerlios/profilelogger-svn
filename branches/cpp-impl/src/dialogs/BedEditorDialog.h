/* 
 * File:   BedEditorDialog.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 14:05
 */

#ifndef _BEDEDITORDIALOG_H
#define	_BEDEDITORDIALOG_H

#include <QDialog>

#include "GrainSizeModes.h"
#include "CarbonateGrainSizeView.h"
#include "LengthMeasurement.h"

class QLabel;
class QDialogButtonBox;
class QGroupBox;
class QFrame;
class QPushButton;
class QTabWidget;

class IdLabel;
class DescriptionEdit;

class Bed;
class OutcropQuality;
class Color;
class Lithology;
class BeddingType;
class BoundaryType;
class CarbonateGrainSize;
class ClasticGrainSize;
class LithologicalUnit;

class OutcropQualityView;
class ColorView;
class LithologyView;
class BeddingTypeView;
class BoundaryTypeView;
class GrainSizeModeSelectorWidget;
class CarbonateGrainSizeView;
class ClasticGrainSizeView;
class ClasticGrainSizeView;
class FaciesView;
class LithologicalUnitView;

class FossilInBedItemModel;
class FossilView;
class FossilInBedView;
class SedimentStructureInBedItemModel;
class SedimentStructureView;
class SedimentStructureInBedView;
class CustomSymbolInBedItemModel;
class CustomSymbolView;
class CustomSymbolInBedView;
class LengthMeasurementWidget;
class BedPropertyPage;

class BedEditorDialog : public QDialog {
    Q_OBJECT
public:
    BedEditorDialog(QWidget* parent, Bed* bed);
    virtual ~BedEditorDialog();

public slots:
    void slotDescriptionChanged(const QString& s);
    void slotOutcropQualityChanged(OutcropQuality* w);
    void slotColorChanged(Color* c);
    void slotLithologyChanged(Lithology* c);
    void slotBeddingTypeChanged(BeddingType* c);
    void slotTopBoundaryTypeChanged(BoundaryType* c);
    void slotGrainSizeModeChanged(GrainSizeModes m);
    void slotBaseCarbonateGrainSizeChanged(CarbonateGrainSize* s);
    void slotTopCarbonateGrainSizeChanged(CarbonateGrainSize* s);
    void slotBaseClasticGrainSizeChanged(ClasticGrainSize* s);
    void slotTopClasticGrainSizeChanged(ClasticGrainSize* s);
    void slotFaciesChanged(Facies* f);
    void slotLithologicalUnitChanged(LithologicalUnit* u);
    
    void slotAddFossils();
    void slotRemoveFossils();
    void slotAddSedimentStructures();
    void slotRemoveSedimentStructures();
    void slotAddCustomSymbols();
    void slotRemoveCustomSymbols();
    void slotCopyGrainSizesFromLithology();
    
    virtual void accept();
    virtual void reject();
    
private:
    void setupGui(QWidget* parent);
    void setupTopBox(QWidget* parent);
    void setupMainBox(QWidget* parent);
    void setupMainSecondaryBox(QWidget* parent);
    void setupHeightWidget(QWidget* parent);
    void setupGrainSizeWidget(QWidget* parent);
    void setupDetailsWidget(QWidget* parent);
    void setupButtons(QWidget* parent);

    void setupOutcropQualityPage();
    void setupColorPage();
    void setupLithologyPage();
    void setupBeddingTypePage();
    void setupBoundaryTypePage();
    void setupCarbonateGrainSizePage();
    void setupClasticGrainSizePage();
    void setupFossilsPage();
    void setupSedimentStructuresPage();
    void setupCustomSymbolsPage();
    void setupFaciesPage();
    void setupLithologicalUnitPage();

    void showData();

    QFrame* _mainW;
    QGroupBox* _mainBoxW;
    IdLabel* _idW;
    QLabel* _bedNumberW;
    DescriptionEdit* _descriptionW;
    QDialogButtonBox* _bbW;

    GrainSizeModeSelectorWidget* _grainSizeModesW;
    QPushButton* _copyGrainSizeFromLithologyW;
    
    QGroupBox* _heightB;
    LengthMeasurementWidget* _heightW;

    QTabWidget* _detailsW;

    QWidget* _outcropQualityP;
    OutcropQualityView* _outcropQualityV;

    BedPropertyPage* _colorP;
    ColorView* _colorV;

    BedPropertyPage* _lithologyP;
    LithologyView* _lithologyV;

    BedPropertyPage* _beddingTypeP;
    BeddingTypeView* _beddingTypeV;

    BedPropertyPage* _boundaryTypeP;
    BoundaryTypeView* _topBoundaryTypeV;

    BedPropertyPage* _carbonateGrainSizeP;
    CarbonateGrainSizeView* _baseCarbonateGrainSizeV;
    CarbonateGrainSizeView* _topCarbonateGrainSizeV;

    BedPropertyPage* _clasticGrainSizeP;
    ClasticGrainSizeView* _baseClasticGrainSizeV;
    ClasticGrainSizeView* _topClasticGrainSizeV;

    BedPropertyPage* _fossilP;
    FossilInBedItemModel* _assignedFossilsM;
    FossilView* _availableFossilsV;
    FossilInBedView* _assignedFossilsV;
    QPushButton* _addFossilsW;
    QPushButton* _removeFossilsW;

    BedPropertyPage* _sedimentStructureP;
    SedimentStructureInBedItemModel* _assignedSedimentStructuresM;
    SedimentStructureView* _availableSedimentStructuresV;
    SedimentStructureInBedView* _assignedSedimentStructuresV;
    QPushButton* _addSedimentStructuresW;
    QPushButton* _removeSedimentStructuresW;

    BedPropertyPage* _customSymbolP;
    CustomSymbolInBedItemModel* _assignedCustomSymbolsM;
    CustomSymbolView* _availableCustomSymbolsV;
    CustomSymbolInBedView* _assignedCustomSymbolsV;
    QPushButton* _addCustomSymbolsW;
    QPushButton* _removeCustomSymbolsW;

    BedPropertyPage* _faciesP;
    FaciesView* _faciesV;

    BedPropertyPage* _lithologicalUnitP;
    LithologicalUnitView* _lithologicalUnitV;

    Bed* _bed;
};

#endif	/* _BEDEDITORDIALOG_H */

