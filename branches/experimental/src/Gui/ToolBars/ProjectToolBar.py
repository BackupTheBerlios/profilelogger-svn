from ToolBar import *

from Gui.Widgets.ProjectSelectionComboBox import *

from Model.Project import *

class ProjectToolBar(ToolBar):
    currentProjectChanged = pyqtSignal(Project)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.projectsW = ProjectSelectionComboBox(self)
        self.projectsW.currentDatasetChanged.connect(self.onProjectChange)
        self.addWidget(QLabel(self.tr("Projects:"), self))
        self.addWidget(self.projectsW)
    def onProjectChange(self, p):
        self.currentProjectChanged.emit(p)
