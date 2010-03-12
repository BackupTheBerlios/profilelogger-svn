from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.BeddingTypeItemView import BeddingTypeItemView

class BeddingTypeInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Bedding Type In Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addBeddingTypeEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        QApplication.instance().beddingTypeModel.setProject(self.data.bed.profile.project)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.beddingTypeW.selectDataset(data.beddingType)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        self.beddingTypeW.currentDatasetChanged.connect(self.onBeddingTypeChange)

    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addBeddingTypeEditor(self):
        self.beddingTypeL = self.createMultiLineLabel(self.tr("&Bedding Type"))
        self.beddingTypeW = BeddingTypeItemView(self.contentW, QApplication.instance().beddingTypeModel)
        self.beddingTypeL.setBuddy(self.beddingTypeW)
        self.addLabelWidgetPair(self.beddingTypeL, self.beddingTypeW)
    def onBeddingTypeChange(self, l):
        self.data.beddingType = l
        self.updateName()
    def updateName(self):
        if self.data.beddingType is None:
            self.nameW.setText(self.tr("<Bedding Type not Set>"))
        else:
            self.data.name = unicode(self.tr("%1 - %2: %3").arg(self.data.begin).arg(self.data.end).arg(self.data.beddingType.name))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
