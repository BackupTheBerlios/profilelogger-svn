from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Widgets.LengthInputWidget import *
from Gui.Widgets.PixelInputWidget import *

class ProfileInProfileAssemblyConfigurationDialog(QDialog):
    def __init__(self, parent, profileInProfileAssembly):
        QDialog.__init__(self, parent)
        self.data = profileInProfileAssembly
        self.setupGui()
        self.showData()

    def setupGui(self):
        self.setLayout(QVBoxLayout(self))
        self.contentW = QGroupBox(self.tr("Profile In Profile Assembly Properties"), self)
        self.contentW.setLayout(QHBoxLayout(self.contentW))
        self.containerW = QToolBox(self.contentW)
        self.contentW.layout().addWidget(self.containerW)
        self.configureWidgets()
        self.layout().addWidget(self.contentW)
        self.bbW = QDialogButtonBox(QDialogButtonBox.Close, Qt.Horizontal, self)
        self.layout().addWidget(self.bbW)
        self.bbW.rejected.connect(self.accept)
    def showData(self):
        self.showMarksData()
        self.showGrainSizeData()
        self.showBeddingTypeData()
        self.showBedNumberData()
        self.showBedHeightData()
        self.showFossilData()
        self.showSedimentStructureData()
        self.showCustomSymbolData()
        self.showFaciesData()
        self.showLithologicalUnitData()
        self.showTectonicUnitData()
        self.showStratigraphicUnitData()
    def configureWidgets(self):
        self.configureMarksWidget()
        self.configureGrainSizesWidget()
        self.configureBeddingTypeWidget()
        self.configureBedNumberWidget()
        self.configureBedHeightWidget()
        self.configureFossilsWidget()
        self.configureSedimentStructuresWidget()
        self.configureCustomSymbolsWidget()
        self.configureFaciesWidget()
        self.configureLithologicalUnitsWidget()
        self.configureTectonicUnitsWidget()
        self.configureStratigraphicUnitsWidget()
    def configureMarksWidget(self):
        self.marksW = QWidget(self.containerW)
        self.marksW.setLayout(QVBoxLayout(self.marksW))

        self.showBigHeightMarksW = QCheckBox(self.tr("Show Big Height Marks"), self.marksW)
        self.showSmallHeightMarksW = QCheckBox(self.tr("Show Small Height Marks"), self.marksW)
        self.showBigHeightMarksLabelsW = QCheckBox(self.tr("Show Big Height Mark Labels"), self.marksW)
        self.showSmallHeightMarksLabelsW = QCheckBox(self.tr("Show Small Height Mark Labels"), self.marksW)
        self.bigMarksDistanceW = LengthInputWidget(self, self.tr("Big Marks Distance"))
        self.smallMarksDistanceW = LengthInputWidget(self, self.tr("Small Marks Distance"))

        self.marksW.layout().addWidget(self.showBigHeightMarksW)
        self.marksW.layout().addWidget(self.showSmallHeightMarksW)
        self.marksW.layout().addWidget(self.showBigHeightMarksLabelsW)
        self.marksW.layout().addWidget(self.showSmallHeightMarksLabelsW)
        self.marksW.layout().addWidget(self.bigMarksDistanceW)
        self.marksW.layout().addWidget(self.smallMarksDistanceW)

        self.showBigHeightMarksW.toggled.connect(self.onShowBigHeightMarksToggled)
        self.showSmallHeightMarksW.toggled.connect(self.onShowSmallHeightMarksToggled)
        self.showBigHeightMarksLabelsW.toggled.connect(self.onShowBigHeightMarksLabelToggled)
        self.showSmallHeightMarksLabelsW.toggled.connect(self.onShowSmallHeightMarksLabelToggled)
        self.bigMarksDistanceW.valueChanged.connect(self.onBigMarksDistanceValueChange)
        self.smallMarksDistanceW.valueChanged.connect(self.onSmallMarksDistanceValueChange)
        self.bigMarksDistanceW.lengthUnitChanged.connect(self.onBigMarksDistanceLengthUnitChange)
        self.smallMarksDistanceW.lengthUnitChanged.connect(self.onSmallMarksDistanceLengthUnitChange)

        self.containerW.addItem(self.marksW, self.tr("Height Marks"))
    def onShowBigHeightMarksToggled(self, toggled):
        self.data.showBigHeightMarks = toggled
    def onShowSmallHeightMarksToggled(self, toggled):
        self.data.showSmallHeightMarks = toggled
    def onShowBigHeightMarksLabelToggled(self, toggled):
        self.data.showBigHeightMarkLabels = toggled
    def onShowSmallHeightMarksLabelToggled(self, toggled):
        self.data.showSmallHeightMarkLabels = toggled
    def onBigMarksDistanceValueChange(self, v):
        self.data.bigHeightMarksDistanceValue = v
    def onBigMarksDistanceLengthUnitChange(self, u):
        self.data.bigHeightMarksDistanceLengthUnit = u    
    def onSmallMarksDistanceValueChange(self, v):
        self.data.smallHeightMarksDistanceValue = v
    def onSmallMarksDistanceLengthUnitChange(self, u):
        self.data.smallHeightMarksDistanceLengthUnit = u
    def showMarksData(self):
        if self.data.showBigHeightMarks:
            self.showBigHeightMarksW.setCheckState(Qt.Checked)
        if self.data.showSmallHeightMarks:
            self.showSmallHeightMarksW.setCheckState(Qt.Checked)
        if self.data.showBigHeightMarkLabels:
            self.showBigHeightMarksLabelsW.setCheckState(Qt.Checked)        
        if self.data.showSmallHeightMarkLabels:
            self.showSmallHeightMarksLabelsW.setCheckState(Qt.Checked)
        self.bigMarksDistanceW.setValue(self.data.bigHeightMarksDistanceValue, self.data.bigHeightMarksDistanceLengthUnit)
        self.smallMarksDistanceW.setValue(self.data.smallHeightMarksDistanceValue, self.data.smallHeightMarksDistanceLengthUnit)
    def configureGrainSizesWidget(self):
        self.grainSizeW = QWidget(self.containerW)
        self.grainSizeW.setLayout(QVBoxLayout(self.grainSizeW))
        self.showGrainSizeW = QCheckBox(self.tr("Show Grain Size Column"), self.grainSizeW)
        self.grainSizesColumnWidthW = PixelInputWidget(self.grainSizeW, self.tr("Grain Size Column Width"))
        self.grainSizeW.layout().addWidget(self.grainSizesColumnWidthW)
        self.grainSizeW.layout().addWidget(self.showGrainSizeW)
        self.containerW.addItem(self.grainSizeW, self.tr("Grain Sizes"))
        self.showGrainSizeW.toggled.connect(self.onShowGrainSizeToggled)
        self.grainSizesColumnWidthW.valueChanged.connect(self.onGrainSizesColumnWidthChange)
    def onGrainSizesColumnWidthChange(self, v):
        self.data.grainSizesColumnWidth = v
    def showGrainSizeData(self):
        if self.data.showGrainSize:
            self.showGrainSizeW.setCheckState(Qt.Checked)
        self.grainSizesColumnWidthW.setValue(self.data.grainSizesColumnWidth)
    def onShowGrainSizeToggled(self, toggled):
        self.data.showGrainSize = toggled
    def configureBeddingTypeWidget(self):
        self.beddingTypeW = QWidget(self.containerW)
        self.beddingTypeW.setLayout(QVBoxLayout(self.beddingTypeW))
        self.showBeddingTypeInColumnW = QCheckBox(self.tr("Show Bedding Type Column"), self.beddingTypeW)
        self.showBeddingTypeInGrainSizeColumnW = QCheckBox(self.tr("Show Bedding Type in Grain Size Column"), self.beddingTypeW)
        self.showBeddingTypeNumberW = QCheckBox(self.tr("Show Bedding Type Number"), self.beddingTypeW)
        self.beddingTypesColumnWidthW = PixelInputWidget(self.beddingTypeW, self.tr("Bedding Types Column Width:"))
        self.beddingTypeW.layout().addWidget(self.beddingTypesColumnWidthW)
        self.beddingTypeW.layout().addWidget(self.showBeddingTypeInColumnW)
        self.beddingTypeW.layout().addWidget(self.showBeddingTypeInGrainSizeColumnW)
        self.beddingTypeW.layout().addWidget(self.showBeddingTypeNumberW)

        self.containerW.addItem(self.beddingTypeW, self.tr("Bedding Type"))
        self.showBeddingTypeInColumnW.toggled.connect(self.onShowBeddingTypeInColumnToggled)
        self.showBeddingTypeInGrainSizeColumnW.toggled.connect(self.onShowBeddingTypeInGrainSizeColumnToggled)
        self.showBeddingTypeNumberW.toggled.connect(self.onShowBeddingTypeNumberToggled)
        self.beddingTypesColumnWidthW.valueChanged.connect(self.onBeddingTypesColumnWidthChanged)
    def onBeddingTypesColumnWidthChanged(self, v):
        self.data.beddingTypesColumnWidth = v
    def onShowBeddingTypeInColumnToggled(self, toggled):
        self.data.showBeddingTypeInColumn = toggled
    def onShowBeddingTypeInGrainSizeColumnToggled(self, toggled):
        self.data.showBeddingTypeInGrainSizeColumn = toggled
    def onShowBeddingTypeNumberToggled(self, toggled):
        self.data.showBeddingTypeNumber = toggled
    def showBeddingTypeData(self):
        if self.data.showBeddingTypeInColumn:
            self.showBeddingTypeInColumnW.setCheckState(Qt.Checked)
        if self.data.showBeddingTypeInGrainSizeColumn:
            self.showBeddingTypeInGrainSizeColumnW.setCheckState(Qt.Checked)
        if self.data.showBeddingTypeNumber:
            self.showBeddingTypeNumberW.setCheckState(Qt.Checked)
        self.beddingTypesColumnWidthW.setValue(self.data.beddingTypesColumnWidth)
    def configureBedNumberWidget(self):
        self.bedNumberW = QWidget(self.containerW)
        self.bedNumberW.setLayout(QVBoxLayout(self.bedNumberW))

        self.showBedNumberInColumnW = QCheckBox(self.tr("Show Bed Number In Column"), self.bedNumberW)
        self.showBedNumberInLithologyW = QCheckBox(self.tr("Show Bed Number In Lithology"), self.bedNumberW)
        self.bedNumberW.layout().addWidget(self.showBedNumberInColumnW)
        self.bedNumberW.layout().addWidget(self.showBedNumberInLithologyW)
        self.containerW.addItem(self.bedNumberW, self.tr("Bed Numbers"))
        self.showBedNumberInColumnW.toggled.connect(self.onShowBedNumberInColumnToggled)
        self.showBedNumberInLithologyW.toggled.connect(self.onShowBedNumberInLithologyToggled)
        self.bedNumberColumnsWidthW = PixelInputWidget(self.bedNumberW, self.tr("Bed Numbers Column Width:"))
        self.bedNumberColumnsWidthW.valueChanged.connect(self.onBedNumberColumnWidthChanged)
        self.bedNumberW.layout().addWidget(self.bedNumberColumnsWidthW)
    def onBedNumberColumnWidthChanged(self, v):
        self.data.bedNumbersColumnWidth = v
    def onShowBedNumberInColumnToggled(self, toggled):
        self.data.showBedNumberInColumn = toggled
    def onShowBedNumberInLithologyToggled(self, toggled):
        self.data.showBedNumberInLithology = toggled
    def showBedNumberData(self):
        if self.data.showBedNumberInColumn:
            self.showBedNumberInColumnW.setCheckState(Qt.Checked)
        if self.data.showBedNumberInLithology:
            self.showBedNumberInLithologyW.setCheckState(Qt.Checked)
        self.bedNumberColumnsWidthW.setValue(self.data.bedNumbersColumnWidth)
    def configureBedHeightWidget(self):
        self.bedHeightW = QWidget(self.containerW)
        self.bedHeightW.setLayout(QVBoxLayout(self.bedHeightW))
        self.showBedHeightInColumnW = QCheckBox(self.tr("Show Bed Height In Column"), self.bedHeightW)
        self.showBedHeightInLithologyW = QCheckBox(self.tr("Show Bed Height In Lithology"), self.bedHeightW)
        self.bedHeightW.layout().addWidget(self.showBedHeightInColumnW)
        self.bedHeightW.layout().addWidget(self.showBedHeightInLithologyW)
        self.containerW.addItem(self.bedHeightW, self.tr("Bed Height"))
        self.showBedHeightInColumnW.toggled.connect(self.onShowBedHeightInColumnToggled)
        self.showBedHeightInLithologyW.toggled.connect(self.onShowBedHeightInLithologyToggled)        
        self.bedHeightsColumnWidthW = PixelInputWidget(self.bedHeightW, self.tr("Bed Height Column Width:"))
        self.bedHeightsColumnWidthW.valueChanged.connect(self.onBedHeightColumnWidthChanged)
        self.bedHeightW.layout().addWidget(self.bedHeightsColumnWidthW)
    def onBedHeightColumnWidthChanged(self, v):
        self.data.bedHeightsColumnWidth = v
    def onShowBedHeightInColumnToggled(self, toggled):
        self.data.showBedHeightInColumn = toggled
    def onShowBedHeightInLithologyToggled(self, toggled):
        self.data.showBedHeightInLithology = toggled
    def showBedHeightData(self):
        if self.data.showBedHeightInColumn:
            self.showBedHeightInColumnW.setCheckState(Qt.Checked)
        if self.data.showBedHeightInLithology:
            self.showBedHeightInLithologyW.setCheckState(Qt.Checked)
        self.bedHeightsColumnWidthW.setValue(self.data.bedHeightsColumnWidth)
    def configureFossilsWidget(self):
        self.fossilsW = QWidget(self.containerW)
        self.fossilsW.setLayout(QVBoxLayout(self.fossilsW))
        self.showFossilsInColumnW = QCheckBox(self.tr("Show Fossils In Column"), self.fossilsW)
        self.showFossilsInBeddingTypeW = QCheckBox(self.tr("Show Fossils In Bedding Type"), self.fossilsW)
        self.showFossilsInLithologyW = QCheckBox(self.tr("Show Fossils In Lithology"), self.fossilsW)
        self.fossilsW.layout().addWidget(self.showFossilsInColumnW)
        self.fossilsW.layout().addWidget(self.showFossilsInBeddingTypeW)
        self.fossilsW.layout().addWidget(self.showFossilsInLithologyW)
        self.containerW.addItem(self.fossilsW, self.tr("Fossils"))
        self.showFossilsInColumnW.toggled.connect(self.onShowFossilsInColumnToggled)
        self.showFossilsInBeddingTypeW.toggled.connect(self.onShowFossilsInBeddingTypeToggled)
        self.showFossilsInLithologyW.toggled.connect(self.onShowFossilsInLithologyToggled)        
        self.fossilsColumnWidthW = PixelInputWidget(self.fossilsW, self.tr("Fossils Column Width:"))
        self.fossilsColumnWidthW.valueChanged.connect(self.onFossilsColumnWidthChanged)
        self.fossilsW.layout().addWidget(self.fossilsColumnWidthW)
    def onFossilsColumnWidthChanged(self, v):
        self.data.fossilsColumnWidth = v
    def onShowFossilsInColumnToggled(self, toggled):
        self.data.showFossilsInColumn = toggled
    def onShowFossilsInBeddingTypeToggled(self, toggled):
        self.data.showFossilsInBeddingType = toggled
    def onShowFossilsInLithologyToggled(self, toggled):
        self.data.showFossilsInLithology = toggled
    def showFossilData(self):
        if self.data.showFossilsInColumn:
            self.showFossilsInColumnW.setCheckState(Qt.Checked)
        if self.data.showFossilsInBeddingType:
            self.showFossilsInBeddingTypeW.setCheckState(Qt.Checked)
        if self.data.showFossilsInLithology:
            self.showFossilsInLithologyW.setCheckState(Qt.Checked)
        self.fossilsColumnWidthW.setValue(self.data.fossilsColumnWidth)
    def configureSedimentStructuresWidget(self):
        self.sedimentStructuresW = QWidget(self.containerW)
        self.sedimentStructuresW.setLayout(QVBoxLayout(self.sedimentStructuresW))
        self.showSedimentStructuresInColumnW = QCheckBox(self.tr("Show Sediment Structures In Column"), self.sedimentStructuresW)
        self.showSedimentStructuresInBeddingTypeW = QCheckBox(self.tr("Show Sediment Structures In Bedding Type"), self.sedimentStructuresW)
        self.showSedimentStructuresInLithologyW = QCheckBox(self.tr("Show Sediment Structures In Lithology"), self.sedimentStructuresW)
        self.sedimentStructuresW.layout().addWidget(self.showSedimentStructuresInColumnW)
        self.sedimentStructuresW.layout().addWidget(self.showSedimentStructuresInBeddingTypeW)
        self.sedimentStructuresW.layout().addWidget(self.showSedimentStructuresInLithologyW)
        self.containerW.addItem(self.sedimentStructuresW, self.tr("Sediment Structures"))
        self.showSedimentStructuresInColumnW.toggled.connect(self.onShowSedimentStructuresInColumnToggled)
        self.showSedimentStructuresInBeddingTypeW.toggled.connect(self.onShowSedimentStructuresInBeddingTypeToggled)
        self.showSedimentStructuresInLithologyW.toggled.connect(self.onShowSedimentStructuresInLithologyToggled)
        self.sedimentStructuresColumnWidthW = PixelInputWidget(self.sedimentStructuresW, self.tr("Sediment Structure Column Width:"))
        self.sedimentStructuresColumnWidthW.valueChanged.connect(self.onSedimentStructureColumnWidthChanged)
        self.sedimentStructuresW.layout().addWidget(self.sedimentStructuresColumnWidthW)
    def onSedimentStructureColumnWidthChanged(self, v):
        self.data.sedimentStructuresColumnWidth = v
    def onShowSedimentStructuresInColumnToggled(self, toggled):
        self.data.showSedimentStructuresInColumn = toggled
    def onShowSedimentStructuresInBeddingTypeToggled(self, toggled):
        self.data.showSedimentStructuresInBeddingType = toggled
    def onShowSedimentStructuresInLithologyToggled(self, toggled):
        self.data.showSedimentStructuresInLithology = toggled
    def showSedimentStructureData(self):
        if self.data.showSedimentStructuresInColumn:
            self.showSedimentStructuresInColumnW.setCheckState(Qt.Checked)
        if self.data.showSedimentStructuresInBeddingType:
            self.showSedimentStructuresInBeddingTypeW.setCheckState(Qt.Checked)
        if self.data.showSedimentStructuresInLithology:
            self.showSedimentStructuresInLithologyW.setCheckState(Qt.Checked)
        self.sedimentStructuresColumnWidthW.setValue(self.data.sedimentStructuresColumnWidth)
    def configureCustomSymbolsWidget(self):
        self.customSymbolsW = QWidget(self.containerW)
        self.customSymbolsW.setLayout(QVBoxLayout(self.customSymbolsW))
        self.showCustomSymbolsInColumnW = QCheckBox(self.tr("Show Custom Symbols In Column"), self.customSymbolsW)
        self.showCustomSymbolsInBeddingTypeW = QCheckBox(self.tr("Show Custom Symbols In Bedding Type"), self.customSymbolsW)
        self.showCustomSymbolsInLithologyW = QCheckBox(self.tr("Show Custom Symbols In Lithology"), self.customSymbolsW)
        self.customSymbolsW.layout().addWidget(self.showCustomSymbolsInColumnW)
        self.customSymbolsW.layout().addWidget(self.showCustomSymbolsInBeddingTypeW)
        self.customSymbolsW.layout().addWidget(self.showCustomSymbolsInLithologyW)
        self.containerW.addItem(self.customSymbolsW, self.tr("Custom Symbols"))
        self.showCustomSymbolsInColumnW.toggled.connect(self.onShowCustomSymbolsInColumnToggled)
        self.showCustomSymbolsInBeddingTypeW.toggled.connect(self.onShowCustomSymbolsInBeddingTypeToggled)
        self.showCustomSymbolsInLithologyW.toggled.connect(self.onShowCustomSymbolsInLithologyToggled)
        self.customSymbolsColumnWidthW = PixelInputWidget(self.customSymbolsW, self.tr("Custom Symbols Column Width:"))
        self.customSymbolsColumnWidthW.valueChanged.connect(self.onCustomSymbolColumnWidthChanged)
        self.customSymbolsW.layout().addWidget(self.customSymbolsColumnWidthW)
    def onCustomSymbolColumnWidthChanged(self, v):
        self.data.customSymbolsColumnWidth = v
    def onShowCustomSymbolsInColumnToggled(self, toggled):
        self.data.showCustomSymbolsInColumn = toggled
    def onShowCustomSymbolsInBeddingTypeToggled(self, toggled):
        self.data.showCustomSymbolsInBeddingType = toggled
    def onShowCustomSymbolsInLithologyToggled(self, toggled):
        self.data.showCustomSymbolsInLithology = toggled
    def showCustomSymbolData(self):
        if self.data.showCustomSymbolsInColumn:
            self.showCustomSymbolsInColumnW.setCheckState(Qt.Checked)
        if self.data.showCustomSymbolsInBeddingType:
            self.showCustomSymbolsInBeddingTypeW.setCheckState(Qt.Checked)
        if self.data.showCustomSymbolsInLithology:
            self.showCustomSymbolsInLithologyW.setCheckState(Qt.Checked)
        self.customSymbolsColumnWidthW.setValue(self.data.customSymbolsColumnWidth)
    def configureFaciesWidget(self):
        self.faciesW = QWidget(self.containerW)
        self.faciesW.setLayout(QVBoxLayout(self.faciesW))
        self.showFaciesInColumnW = QCheckBox(self.tr("Show Facies In Column"), self.faciesW)
        self.faciesW.layout().addWidget(self.showFaciesInColumnW)
        self.containerW.addItem(self.faciesW, self.tr("Facies"))
        self.showFaciesInColumnW.toggled.connect(self.onShowFaciesInColumnToggled)
        self.faciesColumnWidthW = PixelInputWidget(self.faciesW, self.tr("Facies Column Width:"))
        self.faciesColumnWidthW.valueChanged.connect(self.onFaciesColumnWidthChanged)
        self.faciesW.layout().addWidget(self.faciesColumnWidthW)
    def onFaciesColumnWidthChanged(self, v):
        self.data.faciesColumnWidth = v
    def onShowFaciesInColumnToggled(self, toggled):
        self.data.showFaciesInColumn = toggled
    def showFaciesData(self):
        if self.data.showFaciesInColumn:
            self.showFaciesInColumnW.setCheckState(Qt.Checked)
        self.faciesColumnWidthW.setValue(self.data.faciesColumnWidth)
    def configureLithologicalUnitsWidget(self):
        self.lithologicalUnitsW = QWidget(self.containerW)
        self.lithologicalUnitsW.setLayout(QVBoxLayout(self.lithologicalUnitsW))
        self.showLithologicalUnitInColumnW = QCheckBox(self.tr("Show Lithological Units In Column"), self.lithologicalUnitsW)
        self.lithologicalUnitsW.layout().addWidget(self.showLithologicalUnitInColumnW)
        self.containerW.addItem(self.lithologicalUnitsW, self.tr("Lithological Units"))
        self.showLithologicalUnitInColumnW.toggled.connect(self.onShowLithologicalUnitInColumnToggled)
        self.lithologicalUnitsColumnWidthW = PixelInputWidget(self.lithologicalUnitsW, self.tr("Lithological Units Column Width:"))
        self.lithologicalUnitsColumnWidthW.valueChanged.connect(self.onLithologicalUnitsColumnWidthChanged)
        self.lithologicalUnitsW.layout().addWidget(self.lithologicalUnitsColumnWidthW)
    def onLithologicalUnitsColumnWidthChanged(self, v):
        self.data.lithologicalUnitsColumnWidth = v
    def onShowLithologicalUnitInColumnToggled(self, toggled):
        self.data.showLithologicalUnitInColumn = toggled
    def showLithologicalUnitData(self):
        if self.data.showLithologicalUnitInColumn:
            self.showLithologicalUnitInColumnW.setCheckState(Qt.Checked)
        self.lithologicalUnitsColumnWidthW.setValue(self.data.lithologicalUnitsColumnWidth)
    def configureTectonicUnitsWidget(self):
        self.tectonicUnitsW = QWidget(self.containerW)
        self.tectonicUnitsW.setLayout(QVBoxLayout(self.tectonicUnitsW))
        self.showTectonicUnitInColumnW = QCheckBox(self.tr("Show Tectonic Units In Column"), self.tectonicUnitsW)
        self.tectonicUnitsW.layout().addWidget(self.showTectonicUnitInColumnW)
        self.containerW.addItem(self.tectonicUnitsW, self.tr("Tectonic Units"))
        self.showTectonicUnitInColumnW.toggled.connect(self.onShowTectonicUnitInColumnToggled)        
        self.tectonicUnitsColumnWidthW = PixelInputWidget(self.tectonicUnitsW, self.tr("Tectonic Units Column Width:"))
        self.tectonicUnitsColumnWidthW.valueChanged.connect(self.onTectonicUnitsColumnWidthChanged)
        self.tectonicUnitsW.layout().addWidget(self.tectonicUnitsColumnWidthW)
    def onTectonicUnitsColumnWidthChanged(self, v):
        self.data.tectonicUnitsColumnWidth = v
    def onShowTectonicUnitInColumnToggled(self, toggled):
        self.data.showTectonicUnitInColumn = toggled
    def showTectonicUnitData(self):
        if self.data.showTectonicUnitInColumn:
            self.showTectonicUnitInColumnW.setCheckState(Qt.Checked)
        self.tectonicUnitsColumnWidthW.setValue(self.data.tectonicUnitsColumnWidth)
    def configureStratigraphicUnitsWidget(self):
        self.stratigraphicUnitsW = QWidget(self.containerW)
        self.stratigraphicUnitsW.setLayout(QVBoxLayout(self.stratigraphicUnitsW))
        self.showStratigraphicUnitInColumnW = QCheckBox(self.tr("Show Stratigraphic Units In Column"), self.stratigraphicUnitsW)
        self.stratigraphicUnitsW.layout().addWidget(self.showStratigraphicUnitInColumnW)
        self.containerW.addItem(self.stratigraphicUnitsW, self.tr("Stratigraphic Units"))
        self.showStratigraphicUnitInColumnW.toggled.connect(self.onShowStratigraphicUnitInColumnToggled)
        self.stratigraphicUnitsColumnWidthW = PixelInputWidget(self.stratigraphicUnitsW, self.tr("Stratigraphic Units Column Width:"))
        self.stratigraphicUnitsColumnWidthW.valueChanged.connect(self.onStratigraphicUnitsColumnWidthChanged)
        self.stratigraphicUnitsW.layout().addWidget(self.stratigraphicUnitsColumnWidthW)
    def onStratigraphicUnitsColumnWidthChanged(self, v):
        self.data.stratigraphicUnitsColumnWidth = v
    def onShowStratigraphicUnitInColumnToggled(self, toggled):
        self.data.showStratigraphicUnitInColumn = toggled
    def showStratigraphicUnitData(self):
        if self.data.showStratigraphicUnitInColumn:
            self.showStratigraphicUnitInColumnW.setCheckState(Qt.Checked)
        self.stratigraphicUnitsColumnWidthW.setValue(self.data.stratigraphicUnitsColumnWidth)
