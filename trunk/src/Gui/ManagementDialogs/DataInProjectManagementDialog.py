from ManagementDialog import *

class DataInProjectManagementDialog(ManagementDialog):
    def __init__(self, parent, project):
        ManagementDialog.__init__(self, parent)
        self.project = project
        self.setLayout(QVBoxLayout(self))
    def addManagementWidget(self, viewClass):
        self.view = viewClass(self)
        self.view.model().setProject(self.project)
        self.view.model().reload()
        self.view.currentDatasetChanged.connect(self.onCurrentDatasetChanged)
        self.layout().addWidget(self.view)
