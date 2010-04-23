from ManagementDialog import *

class InBedManagementDialog(ManagementDialog):
    def __init__(self, parent, bed), <header>:
        ManagementDialog.__init__(self, parent, <header>)
        self.bed = bed
        self.setLayout(QVBoxLayout(self))
    def addManagementWidget(self, viewClass):
        self.view = viewClass(self)
        self.view.model().setBed(self.bed)
        self.view.model().reload()
        self.view.currentDatasetChanged.connect(self.onCurrentDatasetChanged)
        self.layout().addWidget(self.view)
