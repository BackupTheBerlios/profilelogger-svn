from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.OutcropTypeItemView import OutcropTypeItemView

class OutcropTypeInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Outcrop Type In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addOutcropTypeEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.outcropTypeW.selectDataset(data.outcropType)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.outcropTypeW.currentDatasetChanged.connect(self.onOutcropTypeChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addOutcropTypeEditor(self):
        self.outcropTypeL = self.createMultiLineLabel(self.tr("&Outcrop Type"))
        self.outcropTypeW = OutcropTypeItemView(self.contentW)
        self.outcropTypeL.setBuddy(self.outcropTypeW)
        self.addLabelWidgetPair(self.outcropTypeL, self.outcropTypeW)
        self.outcropTypeW.setProject(self.data.bed.profile.project)
    def onOutcropTypeChange(self, l):
        self.data.outcropType = l
        self.updateName()
    def updateName(self):
        if self.data.outcropType is None:
            self.nameW.setText(self.tr("<Outcrop Type not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.outcropType.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
