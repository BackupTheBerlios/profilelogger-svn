from ManagementDialog import *

class InProfileManagementDialog(ManagementDialog):
    def __init__(self, parent, profile, <header>):
        ManagementDialog.__init__(self, parent, <header>)
        self.profile = profile
        self.setLayout(QVBoxLayout(self))
    def addManagementWidget(self, viewClass):
        self.view = viewClass(self)
        self.view.model().setProfile(self.profile)
        self.view.model().reload()
        self.view.currentDatasetChanged.connect(self.onCurrentDatasetChanged)
        self.layout().addWidget(self.view)
