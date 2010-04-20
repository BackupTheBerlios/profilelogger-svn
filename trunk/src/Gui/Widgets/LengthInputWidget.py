from PyQt4.QtGui import *
from PyQt4.QtCore import *

from IntLineEdit import IntLineEdit
from Model.LengthUnit import LengthUnit

from LengthUnitSelectionComboBox import *

class LengthInputWidget(QWidget):
    valueChanged = pyqtSignal(int)
    lengthUnitChanged = pyqtSignal(LengthUnit)

    def __init__(self, parent, labelText=None):
        QWidget.__init__(self, parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(QHBoxLayout(self))
        self.data = dict()
        self.valueW = IntLineEdit(self)
        self.unitsW = LengthUnitSelectionComboBox(self)
        self.unitsW.reload()

        if labelText is not None:
            self.layout().addWidget(QLabel(labelText, self))
        self.layout().addWidget(self.valueW)
        self.layout().addWidget(self.unitsW)

        self.valueW.valueChanged.connect(self.onValueChange)
        self.unitsW.currentDatasetChanged.connect(self.onUnitActivate)
    def onValueChange(self, val):
        self.valueChanged.emit(val)
    def onUnitActivate(self, val):
        self.lengthUnitChanged.emit(val)
    def setValue(self, val, unit):
        self.valueW.setValue(val)
        self.unitsW.selectDataset(unit)
        print self.__class__.__name__,": ",unit
    def reload(self):
        self.unitsW.reload()
