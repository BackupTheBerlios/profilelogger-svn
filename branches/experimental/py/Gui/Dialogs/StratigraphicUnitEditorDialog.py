from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.StratigraphicUnitTypeItemView import StratigraphicUnitTypeItemView
from Gui.Widgets.LengthRangeInputWidget import LengthRangeInputWidget

class StratigraphicUnitEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Stratigraphic Unit"))
        self.createCustomWidgets()

        self.addIdDisplay()
        self.addNameEdit()        
        self.addLabelWidgetPair(self.typeL, self.typeW)
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))
        self.typeW.selectDataset(self.data.stratigraphicUnitType)

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.typeW.currentDatasetChanged.connect(self.onStratigraphicUnitTypeChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def onStratigraphicUnitTypeChange(self, t):
        self.data.stratigraphicUnitType = t
    def createCustomWidgets(self):
        self.typeL = self.createOneLineLabel(self.tr("Stratigraphic Unit Type"))
        self.typeW = StratigraphicUnitTypeItemView(self.contentW,
                                           QApplication.instance().stratigraphicUnitTypeModel)

        self.sizeRangeL = self.createOneLineLabel(self.tr("Size Range"))
        self.sizeRangeW = LengthRangeInputWidget(self.contentW)
