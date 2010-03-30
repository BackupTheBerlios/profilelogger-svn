from Gui.Dialogs.DatasetInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeTypeInProfileManagementItemView import GrainSizeTypeInProfileManagementItemView
from Gui.Widgets.LengthInputWidget import *
from Gui.Widgets.IntLineEdit import *

class ProfileEditorDialog(DatasetInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetInProjectEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Profile"))
        self.addIdDisplay()
        self.addProjectSelector()
        self.addNameEdit()
        self.addBaseHeightEditor()
        self.addScaleEditor()
        self.addBigMarksEditor()
        self.addSmallMarksEditor()
        self.addGrainSizesEditor()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.projectW.selectDataset(data.project)
        self.nameW.setValue(unicode(self.data.name))
        self.scaleW.setValue(self.data.scale)
        self.bigMarksW.setValue(self.data.bigMarksDistanceValue, self.data.bigMarksDistanceLengthUnit)
        self.smallMarksW.setValue(self.data.smallMarksDistanceValue, self.data.smallMarksDistanceLengthUnit)
        self.baseHeightW.setValue(self.data.startHeightValue, self.data.startHeightLengthUnit)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addBaseHeightEditor(self):
        self.baseHeightL = self.createOneLineLabel(self.tr("Profile starts at height:"))
        self.baseHeightW = LengthInputWidget(self.contentW)
        self.baseHeightL.setBuddy(self.baseHeightW)
        self.addLabelWidgetPair(self.baseHeightL, self.baseHeightW)
        self.baseHeightW.valueChanged.connect(self.onBaseHeightChanged)
        self.baseHeightW.lengthUnitChanged.connect(self.onBaseHeightLengthUnitChanged)
    def addScaleEditor(self):
        self.scaleL = self.createOneLineLabel(self.tr("Scale:"))
        self.scaleW = IntLineEdit(self.contentW)
        self.addLabelWidgetPair(self.scaleL, self.scaleW)
        self.scaleW.valueChanged.connect(self.onScaleChange)
    def onScaleChange(self, v):
        self.data.scale = v
    def onBaseHeightChanged(self, v):
        self.data.startHeightValue = v
    def onBaseHeightLengthUnitChanged(self, u):
        self.data.startHeightLengthUnit = u
    def addGrainSizesEditor(self):
        self.grainSizesL = self.createMultiLineLabel(self.tr("Grain Sizes Types"))
        self.grainSizesW = GrainSizeTypeInProfileManagementItemView(self,
                                                                    QApplication.instance().grainSizeTypeInProfileModel)
        self.addLabelWidgetPair(self.grainSizesL, self.grainSizesW)
        self.grainSizesW.model().setProfile(self.data)
    def addBigMarksEditor(self):
        self.bigMarksL = self.createOneLineLabel(self.tr("Big Marks Distance"))
        self.bigMarksW = LengthInputWidget(self.contentW)
        self.addLabelWidgetPair(self.bigMarksL, self.bigMarksW)
        self.bigMarksW.valueChanged.connect(self.onBigMarksDistanceValueChange)
        self.bigMarksW.lengthUnitChanged.connect(self.onBigMarksDistanceLenghtUnitChange)
    def onBigMarksDistanceValueChange(self, v):
        self.data.bigMarksDistanceValue = v
    def onBigMarksDistanceLenghtUnitChange(self, u):
        self.data.bigMarksDistanceLenghtUnit = u
    def addSmallMarksEditor(self):
        self.smallMarksL = self.createOneLineLabel(self.tr("Small Marks Distance"))
        self.smallMarksW = LengthInputWidget(self.contentW)
        self.addLabelWidgetPair(self.smallMarksL, self.smallMarksW)
        self.smallMarksW.valueChanged.connect(self.onSmallMarksDistanceValueChange)
        self.smallMarksW.lengthUnitChanged.connect(self.onSmallMarksDistanceLenghtUnitChange)
    def onSmallMarksDistanceValueChange(self, v):
        self.data.smallMarksDistanceValue = v
    def onSmallMarksDistanceLenghtUnitChange(self, u):
        self.data.smallMarksDistanceLenghtUnit = u
