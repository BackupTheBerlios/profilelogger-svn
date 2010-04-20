from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProfileAssemblyItemView import ProfileAssemblyItemView

class DatasetInProfileAssemblyEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
    def addProfileAssemblySelector(self):
        self.profileAssemblyL = self.createMultiLineLabel(self.tr("Profile &Assembly"))
        self.profileAssemblyW = ProfileAssemblyItemView(self.contentW)
        self.profileAssemblyL.setBuddy(self.profileAssemblyW)
        self.addLabelWidgetPair(self.profileAssemblyL, self.profileAssemblyW)
        self.profileAssemblyW.currentDatasetChanged.connect(self.onProfileAssemblyChange)
    def onProfileAssemblyChange(self, profileAssembly):
        self.data.profileAssembly = profileAssembly
        self.updateName()
