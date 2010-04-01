from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ManagementDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setLayout(QVBoxLayout(self))
    def addManagementWidget(self, viewClass, modelClass):
        self.view = viewClass(self, modelClass(self))
        self.view.model().reload()
        self.layout().addWidget(self.view)
    def addCloseButton(self):
        self.bb = QDialogButtonBox(QDialogButtonBox.Close, Qt.Horizontal, self)
        self.bb.rejected.connect(self.accept)
        self.layout().addWidget(self.bb)
