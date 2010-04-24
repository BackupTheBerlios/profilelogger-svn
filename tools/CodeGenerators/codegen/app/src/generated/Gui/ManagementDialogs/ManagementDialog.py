from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ManagementDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent, header=None)
        self.setLayout(QVBoxLayout(self))
        self.currentEntity = None
        if header is not None:
            self.headerL = QLabel(header, self)
            self.layout().addWidget(self.headerL)
    def addManagementWidget(self, viewClass):
        self.view = viewClass(self)
        self.view.model().reload()
        self.view.currentEntityChanged.connect(self.onCurrentEntityChanged)
        self.layout().addWidget(self.view)
    def addCloseButton(self):
        self.bb = QDialogButtonBox(QDialogButtonBox.Close, Qt.Horizontal, self)
        self.bb.rejected.connect(self.accept)
        self.layout().addWidget(self.bb)
    def onCurrentEntityChanged(self, ds):
        self.currentEntity = ds
