from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.FossilItemView import FossilItemView

class FossilInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Fossil In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addFossilEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.fossilW.selectDataset(data.fossil)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.fossilW.currentDatasetChanged.connect(self.onFossilChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addFossilEditor(self):
        self.fossilL = self.createMultiLineLabel(self.tr("&Fossil"))
        self.fossilW = FossilItemView(self.contentW)
        self.fossilL.setBuddy(self.fossilW)
        self.addLabelWidgetPair(self.fossilL, self.fossilW)
        self.fossilW.setProject(self.data.bed.profile.project)
    def onFossilChange(self, l):
        self.data.fossil = l
        self.updateName()
    def updateName(self):
        if self.data.fossil is None:
            self.nameW.setText(self.tr("<Fossil not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.fossil.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
