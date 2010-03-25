from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeTypeItemView import GrainSizeTypeItemView
from Gui.Widgets.LengthRangeInputWidget import LengthRangeInputWidget
from Gui.Widgets.PercentEditorWidget import PercentEditorWidget

class GrainSizeEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Grain Size"))
        self.createCustomWidgets()

        self.addIdDisplay()
        self.addNameEdit()        
        self.addLabelWidgetPair(self.typeL, self.typeW)
        self.addLabelWidgetPair(self.sizeRangeL, self.sizeRangeW)
        self.addLabelWidgetPair(self.percentL, self.percentW)
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))
        self.typeW.selectDataset(self.data.grainSizeType)
        self.percentW.setValue(self.data.percentFromMinimum)
        self.sizeRangeW.setRange(self.data.minSize, self.data.minSizeLengthUnit,
                                 self.data.maxSize, self.data.maxSizeLengthUnit)

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.typeW.currentDatasetChanged.connect(self.onGrainSizeTypeChange)
        self.sizeRangeW.minValueChanged.connect(self.onMinValueChange)
        self.sizeRangeW.minLengthUnitChanged.connect(self.onMinLengthUnitChange)
        self.sizeRangeW.maxValueChanged.connect(self.onMaxValueChange)
        self.sizeRangeW.maxLengthUnitChanged.connect(self.onMaxLengthUnitChange)
        self.percentW.valueChanged.connect(self.onPercentFromMinimumChange)
    def onPercentFromMinimumChange(self, v):
        self.data.percentFromMinimum = v
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def onGrainSizeTypeChange(self, t):
        self.data.grainSizeType = t
    def onMinValueChange(self, v):
        self.data.minSize = v
    def onMinLengthUnitChange(self, u):
        self.data.minSizeLengthUnit = u
    def onMaxValueChange(self, v):
        self.data.maxSize = v
    def onMaxLengthUnitChange(self, u):
        self.data.maxSizeLengthUnit = u
    def createCustomWidgets(self):
        self.typeL = self.createOneLineLabel(self.tr("Grain Size Type"))
        self.typeW = GrainSizeTypeItemView(self.contentW,
                                           QApplication.instance().grainSizeTypeModel)

        self.sizeRangeL = self.createOneLineLabel(self.tr("Size Range"))
        self.sizeRangeW = LengthRangeInputWidget(self.contentW)

        self.percentL = self.createOneLineLabel(self.tr("Show at % from Minimum\nin graphic presentation:"))
        self.percentW = PercentEditorWidget(self.contentW)
