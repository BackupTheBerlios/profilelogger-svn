from ToolBar import *

from Gui.Widgets.ProfileColumnSelectionComboBox import *

from Model.ProfileColumn import *

class ProfileColumnToolBar(ToolBar):
    currentProfileColumnChanged = pyqtSignal(ProfileColumn)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.profileColumnsW = ProfileColumnSelectionComboBox(self)
        self.profileColumnsW.currentDatasetChanged.connect(self.onProfileColumnChange)
        self.addWidget(QLabel(self.tr("Profile Columns:"), self))
        self.addWidget(self.profileColumnsW)
    def onProfileColumnChange(self, p):
        self.currentProfileColumnChanged.emit(p)
