from Gui.Dialogs.DatasetInProfileEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProfileColumnItemView import *
from Gui.ItemModels.ProfileColumnItemModel import *

from Gui.Widgets.PixelInputWidget import *
from Gui.Widgets.IntLineEdit import *

class ColumnInProfileEditorDialog(DatasetInProfileEditorDialog):
    def __init__(self, parent, data):
        DatasetInProfileEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Column in Profile"))
        self.addIdDisplay()
        self.addProfileSelector()
        self.addProfileColumnSelector()
        self.addWidthEditor()
        self.addPositionEditor()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.profileW.model().setProject(self.data.profile.project)
        self.profileW.selectDataset(self.data.profile)
        self.profileColumnW.selectDataset(self.data.profileColumn)
        self.widthW.setValue(self.data.width)
        self.positionW.setValue(self.data.position)
    def addProfileColumnSelector(self):
        self.profileColumnL = self.createMultiLineLabel(self.tr("Profile Column"))
        self.profileColumnW = ProfileColumnItemView(self, ProfileColumnItemModel(self))
        self.addLabelWidgetPair(self.profileColumnL, self.profileColumnW)
        self.profileColumnW.model().reload()
        self.profileColumnW.currentDatasetChanged.connect(self.onProfileColumnChange)
    def onProfileColumnChange(self, c):
        self.data.profileColumn = c
    def addWidthEditor(self):
        self.widthL = self.createOneLineLabel(self.tr("Column Width"))
        self.widthW = PixelInputWidget(self.contentW)
        self.addLabelWidgetPair(self.widthL, self.widthW)
        self.widthW.valueChanged.connect(self.onWidthChange)
    def onWidthChange(self, v):
        self.data.width = v
    def addPositionEditor(self):
        self.positionL = self.createOneLineLabel(self.tr("Column Position"))
        self.positionW = IntLineEdit(self.contentW)
        self.addLabelWidgetPair(self.positionL, self.positionW)
        self.positionW.valueChanged.connect(self.onPositionChange)
    def onPositionChange(self, v):
        self.data.position = v
