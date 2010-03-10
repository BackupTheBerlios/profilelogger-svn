from PyQt4.QtGui import *
from PyQt4.QtCore import *

class IntLineEdit(QLineEdit):
    valueChanged = pyqtSignal(int)
    
    def __init__(self, parent):
        QLineEdit.__init__(self, parent)
        self.setValidator(QIntValidator(self))
        self.textChanged.connect(self.onTextChanged)
    def setRange(self, min, max):
        self.validator().setRange(min, max)
    def onTextChanged(self, txt):
        self.valueChanged.emit(QVariant(txt).toInt()[0])
    def setValue(self, intVal):
        self.setText(QVariant(intVal).toString())
