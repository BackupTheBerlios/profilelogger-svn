from ToolBar import *

from Gui.Widgets.ProfileAssemblieselectionComboBox import *

from Model.ProfileAssembly import *

class ProfileAssemblyToolBar(ToolBar):
    currentProfileAssemblyChanged = pyqtSignal(ProfileAssembly)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.profileAssembliesW = ProfileAssemblieselectionComboBox(self)
        self.profileAssembliesW.currentDatasetChanged.connect(self.onProfileAssemblyChange)
        self.addWidget(QLabel(self.tr("Profile Assemblies:"), self))
        self.addWidget(self.profileAssembliesW)
        self.setEnabled(False)
    def onProfileAssemblyChange(self, p):
        self.currentProfileAssemblyChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.profileAssembliesW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
