from ToolBar import *

from Gui.Widgets.ProfileSelectionComboBox import *

from Model.Profile import *

class ProfileToolBar(ToolBar):
    currentProfileChanged = pyqtSignal(Profile)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.profilesW = ProfileSelectionComboBox(self)
        self.profilesW.currentDatasetChanged.connect(self.onProfileChange)
        self.addWidget(QLabel(self.tr("Profiles:"), self))
        self.addWidget(self.profilesW)
        self.setEnabled(False)
    def onProfileChange(self, p):
        self.currentProfileChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.profilesW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
