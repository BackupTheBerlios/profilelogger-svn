from DatasetInProfileEditorDialog import *

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
        self.data.number = v
        self.data.updateName()
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
    def onPageSelectionChange(self, name):
        if name is None:
            return
        for k,v in self.detailPageMap.iteritems():
            if v[0] == name:
                self.stackW.setCurrentWidget(self.detailPages[k])
                return
    def addDetailsWidget(self):
        self.detailsW = QWidget(self.contentW)
        self.detailsW.setLayout(QHBoxLayout(self.detailsW))
        self.pageSelectorW = QListWidget(self.detailsW)
        self.stackW = QStackedWidget(self.detailsW)
        self.pageSelectorW.currentTextChanged.connect(self.onPageSelectionChange)
        self.pageSelectorW.setSortingEnabled(False)
        self.detailsW.layout().addWidget(self.pageSelectorW)
        self.detailsW.layout().addWidget(self.stackW)
        self.contentW.layout().addWidget(self.detailsW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1

        self.detailPageMap = dict()
        self.detailPageMap['lithologies'] = [self.tr("Lithology"), 
                                             LithologyInBedItemView]
        self.detailPageMap['colors'] = [self.tr("Color"), 
                                        ColorInBedItemView]
        self.detailPageMap['bedding types'] = [self.tr("Bedding Type"), 
                                               BeddingTypeInBedItemView]
        self.detailPageMap['custom symbols'] = [self.tr("Custom Symbols"), 
                                                CustomSymbolInBedItemView]
        self.detailPageMap['sediment structure'] = [self.tr("Sediment Structures"), 
                                                    SedimentStructureInBedItemView]
        self.detailPageMap['fossil'] = [self.tr("Fossils"), 
                                        FossilInBedItemView]
        self.detailPageMap['grain sizes'] = [self.tr("Grain Size"), 
                                             GrainSizeInBedItemView]
        self.detailPageMap['boundary types'] = [self.tr("Boundary Type"), 
                                                BoundaryTypeInBedItemView]
        self.detailPageMap['outcrop types'] = [self.tr("Outcrop Type"), 
                                               OutcropTypeInBedItemView]
        self.detailPageMap['facies'] = [self.tr("Facies"), 
                                        FaciesInBedItemView]
        self.detailPageMap['lithological units'] = [self.tr("Lithological Unit"),
                                                    LithologicalUnitInBedItemView]
        self.detailPageMap['geological measurements'] = [self.tr("Geological Measurement"), 
                                                         GeologicalMeasurementInBedItemView]
        self.detailPageMap['lithological units'] = [self.tr("Lithological Unit"),
                                                    LithologicalUnitInBedItemView]
        self.detailPageMap['stratigraphic units'] = [self.tr("Stratigraphic Unit"), 
                                                     StratigraphicUnitInBedItemView]
        self.detailPageMap['tectonic units'] = [self.tr("Tectonic Unit"), 
                                                TectonicUnitInBedItemView]

        self.detailPages = dict()
        for k,v in self.detailPageMap.iteritems():
            print "adding: ",v[1].__name__,": ",unicode(v[0])
            self.detailPages[k] = v[1](self.detailsW)
            self.addDetailPage(self.detailPages[k], v[0])

        self.detailsW.setEnabled(False)
    def addDetailPage(self, page, title):
        self.stackW.addWidget(page)
        self.pageSelectorW.addItem(title)
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
            for k,v in self.detailPageMap.iteritems():
                self.detailPages[k].setBed(self.data)
        else:
            for k,v in self.detailPageMap.iteritems():
                self.detailPages[k].setBed(None)
    def validate(self):
        return self.data.hasValidHeight() and self.data.hasNumber()
