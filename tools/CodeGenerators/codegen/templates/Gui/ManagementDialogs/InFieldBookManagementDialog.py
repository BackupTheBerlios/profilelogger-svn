from ManagementDialog import *

class InFieldBookManagementDialog(ManagementDialog):
    def __init__(self, parent, fieldBook, <header>):
        ManagementDialog.__init__(self, parent, <header>)
        self.fieldBook = fieldBook
        self.setLayout(QVBoxLayout(self))
    def addManagementWidget(self, viewClass):
        self.view = viewClass(self)
        self.view.model().setFieldBook(self.fieldBook)
        self.view.model().reload()
        self.view.currentDatasetChanged.connect(self.onCurrentDatasetChanged)
        self.layout().addWidget(self.view)
