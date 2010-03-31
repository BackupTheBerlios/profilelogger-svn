from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.LithologicalUnitItemView import LithologicalUnitItemView

class LithologicalUnitInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Lithological Unit In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addLithologicalUnitEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        QApplication.instance().lithologicalUnitModel.setProject(self.data.bed.profile.project)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.lithologicalUnitW.selectDataset(data.lithologicalUnit)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.lithologicalUnitW.currentDatasetChanged.connect(self.onLithologicalUnitChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addLithologicalUnitEditor(self):
        self.lithologicalUnitL = self.createMultiLineLabel(self.tr("&Lithological Unit"))
        self.lithologicalUnitW = LithologicalUnitItemView(self.contentW, QApplication.instance().lithologicalUnitModel)
        self.lithologicalUnitL.setBuddy(self.lithologicalUnitW)
        self.addLabelWidgetPair(self.lithologicalUnitL, self.lithologicalUnitW)
    def onLithologicalUnitChange(self, l):
        self.data.lithologicalUnit = l
        self.updateName()
    def updateName(self):
        if self.data.lithologicalUnit is None:
            self.nameW.setText(self.tr("<Lithological Unit not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.lithologicalUnit.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
