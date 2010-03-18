from PyQt4.QtGui import *
from PyQt4.QtCore import *

from IntLineEdit import *

class PixelInputWidget(QWidget):
    valueChanged = pyqtSignal(int)
    
    def __init__(self, parent, label=None):
        QWidget.__init__(self, parent)
        self.setLayout(QHBoxLayout(self))
        if label is not None:
            self.layout().addWidget(QLabel(label, self))
        self.valueW = IntLineEdit(self)
        self.layout().addWidget(self.valueW)
        self.layout().addWidget(QLabel(self.tr("Pixel"), self))
        self.valueW.valueChanged.connect(self.onValueChanged)
    def onValueChanged(self, v):
        self.valueChanged.emit(v)
    def setValue(self, v):
        self.valueW.setValue(v)
