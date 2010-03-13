from Gui.Dialogs.DatasetInProfileEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView
from Gui.ItemViews.LithologyInBedItemView import LithologyInBedItemView
from Gui.ItemViews.ColorInBedItemView import ColorInBedItemView
from Gui.ItemViews.BeddingTypeInBedItemView import BeddingTypeInBedItemView
from Gui.ItemViews.CustomSymbolInBedItemView import CustomSymbolInBedItemView
from Gui.ItemViews.SedimentStructureInBedItemView import SedimentStructureInBedItemView
from Gui.ItemViews.FossilInBedItemView import FossilInBedItemView
from Gui.ItemViews.GrainSizeInBedItemView import GrainSizeInBedItemView
from Gui.ItemViews.BoundaryTypeInBedItemView import BoundaryTypeInBedItemView
from Gui.ItemViews.OutcropTypeInBedItemView import OutcropTypeInBedItemView
from Gui.ItemViews.FaciesInBedItemView import FaciesInBedItemView
from Gui.ItemViews.LithologicalUnitInBedItemView import LithologicalUnitInBedItemView
from Gui.ItemViews.StratigraphicUnitInBedItemView import StratigraphicUnitInBedItemView
from Gui.ItemViews.TectonicUnitInBedItemView import TectonicUnitInBedItemView
from Gui.ItemViews.GeologicalMeasurementInBedItemView import GeologicalMeasurementInBedItemView
from Gui.Widgets.LengthInputWidget import LengthInputWidget
from Gui.Widgets.IntLineEdit import IntLineEdit

class BedEditorDialog(DatasetInProfileEditorDialog):
    def __init__(self, parent, data):
        DatasetInProfileEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addProfileSelector()
        self.addBedNumberEdit()
        self.addHeightEdit()
        self.addDescriptionEdit()
        self.addSaveBedButton()
        self.addDetailsWidget()
        self.addButtons()

        self.nameW.setEnabled(False)
        self.profileW.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.idW.setValue(self.data.id)
        self.profileW.selectDataset(data.profile)
        self.nameW.setValue(unicode(self.data.name))
        self.heightW.setValue(self.data.height, self.data.lengthUnit)
        self.bedNumberW.setValue(self.data.number)
        self.descriptionW.setValue(unicode(self.data.description))
        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.setDetailsWidgetStatus(self.data.hasId())
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addHeightEdit(self):
        self.heightL = self.createOneLineLabel(self.tr("&Height"))
        self.heightW = LengthInputWidget(self.contentW)
        self.heightL.setBuddy(self.heightW)
        self.addLabelWidgetPair(self.heightL, self.heightW)
        self.heightW.valueChanged.connect(self.onHeightValueChange)
        self.heightW.lengthUnitChanged.connect(self.onHeightUnitChange)
    def addBedNumberEdit(self):
        self.bedNumberL = self.createOneLineLabel(self.tr("Bed &Number"))
        self.bedNumberW = IntLineEdit(self.contentW)
        self.bedNumberL.setBuddy(self.bedNumberW)
        self.addLabelWidgetPair(self.bedNumberL, self.bedNumberW)
        self.bedNumberW.valueChanged.connect(self.onBedNumberChange)
    def onBedNumberChange(self, v):
        self.data.name = unicode(self.tr("%1/%2/Bed #%3").arg(self.data.profile.project.name).arg(self.data.profile.name).arg(v, 5, 10, QChar('0')))
        self.data.number = v
        self.nameW.setText(self.data.name)
    def onHeightValueChange(self, v):
        self.data.height = v
    def onHeightUnitChange(self, u):
        self.data.lengthUnit = u
    def addSaveBedButton(self):
        self.saveBedW = QPushButton(self.tr("&Save Bed"), self.contentW)
        self.contentW.layout().addWidget(self.saveBedW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
        self.saveBedW.clicked.connect(self.onSaveRequest)
    def addDetailsWidget(self):
        self.detailsW = QTabWidget(self.contentW)
        self.contentW.layout().addWidget(self.detailsW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1

        self.lithologyInBedW = LithologyInBedItemView(self.detailsW, QApplication.instance().lithologyInBedModel)
        self.colorInBedW = ColorInBedItemView(self.detailsW, QApplication.instance().colorInBedModel)
        self.beddingTypeInBedW = BeddingTypeInBedItemView(self.detailsW, QApplication.instance().beddingTypeInBedModel)
        self.customSymbolInBedW = CustomSymbolInBedItemView(self.detailsW, QApplication.instance().customSymbolInBedModel)
        self.sedimentStructureInBedW = SedimentStructureInBedItemView(self.detailsW, QApplication.instance().sedimentStructureInBedModel)
        self.fossilInBedW = FossilInBedItemView(self.detailsW, QApplication.instance().fossilInBedModel)
        self.grainSizeInBedW = GrainSizeInBedItemView(self.detailsW, QApplication.instance().grainSizeInBedModel)
        self.boundaryTypeInBedW = BoundaryTypeInBedItemView(self.detailsW, QApplication.instance().boundaryTypeInBedModel)
        self.outcropTypeInBedW = OutcropTypeInBedItemView(self.detailsW, QApplication.instance().outcropTypeInBedModel)
        self.faciesInBedW = FaciesInBedItemView(self.detailsW, QApplication.instance().faciesInBedModel)
        self.lithologicalUnitInBedW = LithologicalUnitInBedItemView(self.detailsW, QApplication.instance().lithologicalUnitInBedModel)
        self.stratigraphicUnitInBedW = StratigraphicUnitInBedItemView(self.detailsW, QApplication.instance().stratigraphicUnitInBedModel)
        self.tectonicUnitInBedW = TectonicUnitInBedItemView(self.detailsW, QApplication.instance().tectonicUnitInBedModel)
        self.geologicalMeasurementInBedW = GeologicalMeasurementInBedItemView(self.detailsW, QApplication.instance().geologicalMeasurementInBedModel)

        self.detailsW.addTab(self.lithologyInBedW, self.tr("Lithologies"))
        self.detailsW.addTab(self.colorInBedW, self.tr("Colors"))
        self.detailsW.addTab(self.beddingTypeInBedW, self.tr("Bedding Types"))
        self.detailsW.addTab(self.customSymbolInBedW, self.tr("Custom Symbols"))
        self.detailsW.addTab(self.sedimentStructureInBedW, self.tr("Sediment Structures"))
        self.detailsW.addTab(self.fossilInBedW, self.tr("Fossils"))
        self.detailsW.addTab(self.grainSizeInBedW, self.tr("Grain Sizes"))
        self.detailsW.addTab(self.boundaryTypeInBedW, self.tr("Boundary Types"))
        self.detailsW.addTab(self.outcropTypeInBedW, self.tr("Outcrop Types"))
        self.detailsW.addTab(self.faciesInBedW, self.tr("Facies"))
        self.detailsW.addTab(self.lithologicalUnitInBedW, self.tr("Lithological Units"))
        self.detailsW.addTab(self.stratigraphicUnitInBedW, self.tr("Stratigraphic Units"))
        self.detailsW.addTab(self.tectonicUnitInBedW, self.tr("Tectonic Units"))
        self.detailsW.addTab(self.geologicalMeasurementInBedW, self.tr("Geological Measurements"))
        self.detailsW.setEnabled(False)
    def onSaveRequest(self):
        if self.save():
            self.enableDetailsWidget()
        else:
            self.disableDetailsWidget()
    def enableDetailsWidget(self):
        self.setDetailsWidgetStatus(True)
    def disableDetailsWidget(self):
        self.setDetailsWidgetStatus(False)
    def setDetailsWidgetStatus(self, isEnabled):
        self.detailsW.setEnabled(isEnabled)
        if isEnabled:
            QApplication.instance().lithologyInBedModel.setBed(self.data)
            QApplication.instance().colorInBedModel.setBed(self.data)
            QApplication.instance().beddingTypeInBedModel.setBed(self.data)
            QApplication.instance().customSymbolInBedModel.setBed(self.data)
            QApplication.instance().sedimentStructureInBedModel.setBed(self.data)
            QApplication.instance().fossilInBedModel.setBed(self.data)
            QApplication.instance().grainSizeInBedModel.setBed(self.data)
            QApplication.instance().boundaryTypeInBedModel.setBed(self.data)
            QApplication.instance().outcropTypeInBedModel.setBed(self.data)
            QApplication.instance().faciesInBedModel.setBed(self.data)
            QApplication.instance().lithologicalUnitInBedModel.setBed(self.data)
            QApplication.instance().stratigraphicUnitInBedModel.setBed(self.data)
            QApplication.instance().tectonicUnitInBedModel.setBed(self.data)
            QApplication.instance().geologicalMeasurementInBedModel.setBed(self.data)
        else:
            QApplication.instance().lithologyInBedModel.setBed(None)
            QApplication.instance().colorInBedModel.setBed(None)
            QApplication.instance().beddingTypeInBedModel.setBed(None)
            QApplication.instance().customSymbolInBedModel.setBed(None)
            QApplication.instance().sedimentStructureInBedModel.setBed(None)
            QApplication.instance().fossilInBedModel.setBed(None)
            QApplication.instance().grainSizeInBedModel.setBed(None)
            QApplication.instance().boundaryTypeInBedModel.setBed(None)
            QApplication.instance().outcropTypeInBedModel.setBed(None)
            QApplication.instance().faciesInBedModel.setBed(None)
            QApplication.instance().lithologicalUnitInBedModel.setBed(None)
            QApplication.instance().stratigraphicUnitInBedModel.setBed(None)
            QApplication.instance().tectonicUnitInBedModel.setBed(None)
            QApplication.instance().geologicalMeasurementInBedModel.setBed(None)
