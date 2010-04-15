from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ManagementDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setLayout(QVBoxLayout(self))
        self.currentDataset = None
    def addManagementWidget(self, viewClass):
        self.view = viewClass(self)
        self.view.model().reload()
        self.view.currentDatasetChanged.connect(self.onCurrentDatasetChanged)
        self.layout().addWidget(self.view)
    def addCloseButton(self):
        self.bb = QDialogButtonBox(QDialogButtonBox.Close, Qt.Horizontal, self)
        self.bb.rejected.connect(self.accept)
        self.layout().addWidget(self.bb)
    def onCurrentDatasetChanged(self, ds):
        self.currentDataset = ds
