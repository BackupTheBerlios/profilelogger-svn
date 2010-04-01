from ManagementDialog import *

class DataInProjectManagementDialog(ManagementDialog):
    def __init__(self, parent, project):
        ManagementDialog.__init__(self, parent)
        self.project = project
        self.setLayout(QVBoxLayout(self))
    def addManagementWidget(self, viewClass, modelClass):
        self.view = viewClass(self, modelClass(self))
        self.view.model().setProject(self.project)
        self.view.model().reload()
        self.layout().addWidget(self.view)
