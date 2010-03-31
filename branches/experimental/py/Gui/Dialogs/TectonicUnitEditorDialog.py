from Gui.Dialogs.DatasetWithSvgItemInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.TectonicUnitTypeItemView import TectonicUnitTypeItemView
from Gui.Widgets.LengthRangeInputWidget import LengthRangeInputWidget

class TectonicUnitEditorDialog(DatasetWithSvgItemInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Tectonic Unit"))
        self.createCustomWidgets()

        self.addIdDisplay()
        self.addProjectSelector()
        self.addSvgItemSelector()
        self.addNameEdit()        
        self.addLabelWidgetPair(self.typeL, self.typeW)
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.projectW.selectDataset(data.project)
        self.svgItemW.selectDataset(data.svgItem)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))
        self.typeW.selectDataset(self.data.tectonicUnitType)

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.typeW.currentDatasetChanged.connect(self.onTectonicUnitTypeChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def onTectonicUnitTypeChange(self, t):
        self.data.tectonicUnitType = t
    def createCustomWidgets(self):
        self.typeL = self.createOneLineLabel(self.tr("Tectonic Unit Type"))
        self.typeW = TectonicUnitTypeItemView(self.contentW,
                                           QApplication.instance().tectonicUnitTypeModel)
