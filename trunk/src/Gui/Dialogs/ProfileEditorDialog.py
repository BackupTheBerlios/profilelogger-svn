from Gui.Dialogs.DatasetInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeTypeInProfileManagementItemView import GrainSizeTypeInProfileManagementItemView
from Gui.ItemViews.ColumnInProfileItemView import ColumnInProfileItemView
from Gui.ItemModels.ColumnInProfileItemModel import *

from Gui.Widgets.LengthInputWidget import *
from Gui.Widgets.IntLineEdit import *

class ProfileEditorDialog(DatasetInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetInProjectEditorDialog.__init__(self, parent, data)
        print "big: ",self.data.bigMarksDistanceValue," ",self.data.bigMarksDistanceLengthUnit
        print "small: ",self.data.smallMarksDistanceValue," ",self.data.smallMarksDistanceLengthUnit
        self.addContentPanel(self.tr("Profile"))
        self.addIdDisplay()
        self.addProjectSelector()
        self.addNameEdit()
        self.addBaseHeightEditor()
        self.addScaleEditor()
        self.addBigMarksEditor()
        self.addSmallMarksEditor()
        self.addLegendColumnsEditor()
        self.addGrainSizesEditor()
        self.addColumnEditor()
        self.addDescriptionEdit()
        self.addButtons()

        print "setting: ",self.data.bigMarksDistanceLengthUnit
        self.grainSizesW.reload()
        self.columnsW.reload()

        self.idW.setValue(self.data.id)
        self.projectW.selectDataset(self.data.project)
        self.nameW.setValue(unicode(self.data.name))
        self.scaleW.setValue(self.data.scale)
        self.bigMarksW.setValue(self.data.bigMarksDistanceValue, self.data.bigMarksDistanceLengthUnit)
        self.smallMarksW.setValue(self.data.smallMarksDistanceValue, self.data.smallMarksDistanceLengthUnit)
        self.baseHeightW.setValue(self.data.startHeightValue, self.data.startHeightLengthUnit)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.legendColumnsW.setValue(self.data.colsInLegend)
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
        self.scaleL = self.createOneLineLabel(self.tr("Scale 1:"))
        self.scaleW = IntLineEdit(self.contentW)
        self.addLabelWidgetPair(self.scaleL, self.scaleW)
        self.scaleW.valueChanged.connect(self.onScaleChange)
    def onScaleChange(self, v):
        self.data.scale = v
    def addLegendColumnsEditor(self):
        self.legendColumnsL = self.createOneLineLabel(self.tr("Legend Columns:"))
        self.legendColumnsW = IntLineEdit(self.contentW)
        self.addLabelWidgetPair(self.legendColumnsL, self.legendColumnsW)
        self.legendColumnsW.valueChanged.connect(self.onLegendColumnsChange)
    def onLegendColumnsChange(self, v):
        self.data.colsInLegend = v
    def onBaseHeightChanged(self, v):
        self.data.startHeightValue = v
    def onBaseHeightLengthUnitChanged(self, u):
        self.data.startHeightLengthUnit = u
    def addGrainSizesEditor(self):
        self.grainSizesL = self.createMultiLineLabel(self.tr("Grain Sizes Types"))
        self.grainSizesW = GrainSizeTypeInProfileManagementItemView(self)
        self.addLabelWidgetPair(self.grainSizesL, self.grainSizesW)
        self.grainSizesW.model().setProfile(self.data)
    def addColumnEditor(self):
        self.columnsL = self.createMultiLineLabel(self.tr("Columns"))
        self.columnsW = ColumnInProfileItemView(self)
        self.addLabelWidgetPair(self.columnsL, self.columnsW)
        self.columnsW.model().setProfile(self.data)
    def addBigMarksEditor(self):
        self.bigMarksL = self.createOneLineLabel(self.tr("Big Marks Distance"))
        self.bigMarksW = LengthInputWidget(self.contentW)
        self.addLabelWidgetPair(self.bigMarksL, self.bigMarksW)
        self.bigMarksW.valueChanged.connect(self.onBigMarksDistanceValueChange)
        self.bigMarksW.lengthUnitChanged.connect(self.onBigMarksDistanceLenghtUnitChange)
    def onBigMarksDistanceValueChange(self, v):
        self.data.bigMarksDistanceValue = v
    def onBigMarksDistanceLenghtUnitChange(self, u):
        self.data.bigMarksDistanceLengthUnit = u
        print self.data.bigMarksDistanceLengthUnit
    def addSmallMarksEditor(self):
        self.smallMarksL = self.createOneLineLabel(self.tr("Small Marks Distance"))
        self.smallMarksW = LengthInputWidget(self.contentW)
        self.addLabelWidgetPair(self.smallMarksL, self.smallMarksW)
        self.smallMarksW.valueChanged.connect(self.onSmallMarksDistanceValueChange)
        self.smallMarksW.lengthUnitChanged.connect(self.onSmallMarksDistanceLenghtUnitChange)
    def onSmallMarksDistanceValueChange(self, v):
        self.data.smallMarksDistanceValue = v
    def onSmallMarksDistanceLenghtUnitChange(self, u):
        self.data.smallMarksDistanceLengthUnit = u
        print self.data.smallMarksDistanceLengthUnit
