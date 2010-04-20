from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.LithologyItemView import LithologyItemView

class LithologyInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Lithology In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addLithologyEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.lithologyW.selectDataset(data.lithology)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.lithologyW.currentDatasetChanged.connect(self.onLithologyChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addLithologyEditor(self):
        self.lithologyL = self.createMultiLineLabel(self.tr("&Lithology"))
        self.lithologyW = LithologyItemView(self.contentW)
        self.lithologyL.setBuddy(self.lithologyW)
        self.addLabelWidgetPair(self.lithologyL, self.lithologyW)
        self.lithologyW.setProject(self.data.bed.profile.project)
    def onLithologyChange(self, l):
        self.data.lithology = l
        self.updateName()
    def updateName(self):
        if self.data.lithology is None:
            self.nameW.setText(self.tr("<Lithology not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.lithology.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
