from Gui.Dialogs.DatasetInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView
from Gui.Widgets.LengthInputWidget import *

class ProfileEditorDialog(DatasetInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetInProjectEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Profile"))
        self.addIdDisplay()
        self.addProjectSelector()
        self.addNameEdit()
        self.addBaseHeightEditor()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.projectW.selectDataset(data.project)
        self.nameW.setValue(unicode(self.data.name))
        self.baseHeightW.setValue(self.data.startHeightValue, self.data.startHeightLengthUnit)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addBaseHeightEditor(self):
        self.baseHeightL = QLabel(self.tr("Profile starts at height:"), self.contentW)
        self.baseHeightW = LengthInputWidget(self.contentW)
        self.baseHeightL.setBuddy(self.baseHeightW)
        self.addLabelWidgetPair(self.baseHeightL, self.baseHeightW)
        self.baseHeightW.valueChanged.connect(self.onBaseHeightChanged)
        self.baseHeightW.lengthUnitChanged.connect(self.onBaseHeightLengthUnitChanged)
    def onBaseHeightChanged(self, v):
        self.data.startHeightValue = v
    def onBaseHeightLengthUnitChanged(self, u):
        self.data.startHeightLengthUnit = u

