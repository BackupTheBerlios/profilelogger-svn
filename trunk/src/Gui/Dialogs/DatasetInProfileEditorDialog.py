from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProfileItemView import ProfileItemView

class DatasetInProfileEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
    def addProfileSelector(self):
        self.profileL = self.createMultiLineLabel(self.tr("&Profile"))
        self.profileW = ProfileItemView(self.contentW)
        self.profileL.setBuddy(self.profileW)
        self.addLabelWidgetPair(self.profileL, self.profileW)
        self.profileW.currentDatasetChanged.connect(self.onProfileChange)
        QApplication.instance().profileModel.reload()
    def onProfileChange(self, profile):
        self.data.profile = profile
