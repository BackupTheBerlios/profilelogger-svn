from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ColorItemView import ColorItemView

class ColorInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Color In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addColorEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.colorW.selectDataset(data.color)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.colorW.currentDatasetChanged.connect(self.onColorChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addColorEditor(self):
        self.colorL = self.createMultiLineLabel(self.tr("&Color"))
        self.colorW = ColorItemView(self.contentW)
        self.colorL.setBuddy(self.colorW)
        self.addLabelWidgetPair(self.colorL, self.colorW)
        self.colorW.setProject(self.data.bed.profile.project)
    def onColorChange(self, l):
        self.data.color = l
        self.updateName()
    def updateName(self):
        if self.data.color is None:
            self.nameW.setText(self.tr("<Color not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.color.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
