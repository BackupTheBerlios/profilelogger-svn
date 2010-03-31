from PyQt4.QtGui import *
from PyQt4.QtCore import *

from IntLineEdit import IntLineEdit

class StrikeDipEditorWidget(QWidget):
    strikeChanged = pyqtSignal(int)
    dipChanged = pyqtSignal(int)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setLayout(QHBoxLayout(self))
        self.strikeW = IntLineEdit(self)
        self.dipW = IntLineEdit(self)
        self.strikeW.setRange(0, 360)
        self.dipW.setRange(0, 90)
        self.layout().addWidget(self.strikeW)
        self.layout().addWidget(QLabel("/", self))
        self.layout().addWidget(self.dipW)
        self.strikeW.valueChanged.connect(self.onStrikeChange)
        self.dipW.valueChanged.connect(self.onDipChange)
    def onStrikeChange(self, v):
        self.strikeChanged.emit(v)
    def onDipChange(self, v):
        self.dipChanged.emit(v)
    def setValues(self, strike, dip):
        self.strikeW.setValue(strike)
        self.dipW.setValue(dip)
