from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.SedimentStructureItemView import SedimentStructureItemView

class SedimentStructureInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Sediment Structure In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addSedimentStructureEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        QApplication.instance().sedimentStructureModel.setProject(self.data.bed.profile.project)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.sedimentStructureW.selectDataset(data.sedimentStructure)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.sedimentStructureW.currentDatasetChanged.connect(self.onSedimentStructureChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addSedimentStructureEditor(self):
        self.sedimentStructureL = self.createMultiLineLabel(self.tr("&Sediment Structure"))
        self.sedimentStructureW = SedimentStructureItemView(self.contentW, QApplication.instance().sedimentStructureModel)
        self.sedimentStructureL.setBuddy(self.sedimentStructureW)
        self.addLabelWidgetPair(self.sedimentStructureL, self.sedimentStructureW)
    def onSedimentStructureChange(self, l):
        self.data.sedimentStructure = l
        self.updateName()
    def updateName(self):
        if self.data.sedimentStructure is None:
            self.nameW.setText(self.tr("<Sediment Structure not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.sedimentStructure.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
