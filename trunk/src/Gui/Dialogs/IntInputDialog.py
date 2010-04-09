from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Widgets.IntLineEdit import *

class IntInputDialog(QDialog):
    def __init__(self, parent,
                 lbl,
                 value,
                 min=-2147483647,
                 max=2147483647):
        QDialog.__init__(self, parent)
        self.val = value
        self.setLayout(QVBoxLayout(self))
        self.lbl = QLabel(lbl, self)
        self.w = IntLineEdit(self)
        self.w.setRange(min, max)
        self.w.setValue(value)
        self.bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                   Qt.Horizontal,
                                   self)
        self.layout().addWidget(self.lbl)
        self.layout().addWidget(self.w)
        self.layout().addWidget(self.bb)
        self.w.valueChanged.connect(self.onValueChange)
        self.bb.accepted.connect(self.accept)
        self.bb.rejected.connect(self.reject)
    def onValueChange(self, v):
        self.val = v
    def getValue(self):
        return self.val
