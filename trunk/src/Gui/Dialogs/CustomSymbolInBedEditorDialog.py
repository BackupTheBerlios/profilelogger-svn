from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.CustomSymbolItemView import CustomSymbolItemView

class CustomSymbolInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Custom Symbol In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addCustomSymbolEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.customSymbolW.selectDataset(data.customSymbol)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.customSymbolW.currentDatasetChanged.connect(self.onCustomSymbolChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addCustomSymbolEditor(self):
        self.customSymbolL = self.createMultiLineLabel(self.tr("&Custom Symbol"))
        self.customSymbolW = CustomSymbolItemView(self.contentW)
        self.customSymbolL.setBuddy(self.customSymbolW)
        self.addLabelWidgetPair(self.customSymbolL, self.customSymbolW)
        self.customSymbolW.setProject(self.data.bed.profile.project)
    def onCustomSymbolChange(self, l):
        self.data.customSymbol = l
        self.updateName()
    def updateName(self):
        if self.data.customSymbol is None:
            self.nameW.setText(self.tr("<Custom Symbol not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.customSymbol.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()