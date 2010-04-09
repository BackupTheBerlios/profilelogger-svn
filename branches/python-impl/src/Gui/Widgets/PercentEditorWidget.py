from PyQt4.QtGui import *
from PyQt4.QtCore import*

from IntLineEdit import *

class PercentEditorWidget(QWidget):
    valueChanged = pyqtSignal(int)
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setLayout(QHBoxLayout(self))
        self.valueW = IntLineEdit(self)
        self.valueW.setRange(0, 100)
        self.valueW.valueChanged.connect(self.onValueChange)
    def onValueChange(self, v):
        self.valueChanged.emit(v)
    def setValue(self, v):
        self.valueW.setValue(v)
