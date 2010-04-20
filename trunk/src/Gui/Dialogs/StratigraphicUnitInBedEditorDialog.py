from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.StratigraphicUnitItemView import StratigraphicUnitItemView

class StratigraphicUnitInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Stratigraphic Unit In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addStratigraphicUnitEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.stratigraphicUnitW.selectDataset(data.stratigraphicUnit)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.stratigraphicUnitW.currentDatasetChanged.connect(self.onStratigraphicUnitChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addStratigraphicUnitEditor(self):
        self.stratigraphicUnitL = self.createMultiLineLabel(self.tr("&Stratigraphic Unit"))
        self.stratigraphicUnitW = StratigraphicUnitItemView(self.contentW)
        self.stratigraphicUnitL.setBuddy(self.stratigraphicUnitW)
        self.addLabelWidgetPair(self.stratigraphicUnitL, self.stratigraphicUnitW)
        self.stratigraphicUnitW.setProject(self.data.bed.profile.project)
    def onStratigraphicUnitChange(self, l):
        self.data.stratigraphicUnit = l
        self.updateName()
    def updateName(self):
        if self.data.stratigraphicUnit is None:
            self.nameW.setText(self.tr("<Stratigraphic Unit not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.stratigraphicUnit.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
