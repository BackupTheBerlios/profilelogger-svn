from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.TectonicUnitItemView import TectonicUnitItemView

class TectonicUnitInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Tectonic Unit In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addTectonicUnitEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        QApplication.instance().tectonicUnitModel.setProject(self.data.bed.profile.project)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.tectonicUnitW.selectDataset(data.tectonicUnit)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.tectonicUnitW.currentDatasetChanged.connect(self.onTectonicUnitChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addTectonicUnitEditor(self):
        self.tectonicUnitL = self.createMultiLineLabel(self.tr("&Tectonic Unit"))
        self.tectonicUnitW = TectonicUnitItemView(self.contentW, QApplication.instance().tectonicUnitModel)
        self.tectonicUnitL.setBuddy(self.tectonicUnitW)
        self.addLabelWidgetPair(self.tectonicUnitL, self.tectonicUnitW)
    def onTectonicUnitChange(self, l):
        self.data.tectonicUnit = l
        self.updateName()
    def updateName(self):
        if self.data.tectonicUnit is None:
            self.nameW.setText(self.tr("<Tectonic Unit not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.tectonicUnit.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
