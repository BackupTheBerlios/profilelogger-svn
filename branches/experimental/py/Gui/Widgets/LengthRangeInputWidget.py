from PyQt4.QtGui import *
from PyQt4.QtCore import *

from LengthInputWidget import LengthInputWidget

from Model.LengthUnit import LengthUnit

class LengthRangeInputWidget(QWidget):
    minValueChanged = pyqtSignal(int)
    minLengthUnitChanged = pyqtSignal(LengthUnit)
    maxValueChanged = pyqtSignal(int)
    maxLengthUnitChanged = pyqtSignal(LengthUnit)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setLayout(QHBoxLayout(self))
        self.minW = LengthInputWidget(self)
        self.maxW = LengthInputWidget(self)
        self.spaceW = QLabel(unicode("-"), self)
        self.layout().addWidget(self.minW)
        self.layout().addWidget(self.spaceW)
        self.layout().addWidget(self.maxW)
        
        self.minW.valueChanged.connect(self.onMinValueChange)
        self.minW.lengthUnitChanged.connect(self.onMinLengthUnitChange)
        self.maxW.valueChanged.connect(self.onMaxValueChange)
        self.maxW.lengthUnitChanged.connect(self.onMaxLengthUnitChange)
    def onMinValueChange(self, v):
        self.minValueChanged.emit(v)
    def onMinLengthUnitChange(self, u):
        self.minLengthUnitChanged.emit(u)
    def onMaxValueChange(self, v):
        self.maxValueChanged.emit(v)
    def onMaxLengthUnitChange(self, u):
        self.maxLengthUnitChanged.emit(u)
    def setRange(self, min, minU, max, maxU):
        self.minW.setValue(min, minU)
        self.maxW.setValue(max, maxU)
