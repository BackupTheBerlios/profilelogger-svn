from PyQt4.QtGui import *
from PyQt4.QtCore import *

from IntLineEdit import IntLineEdit
from Model.LengthUnit import LengthUnit

class LengthInputWidget(QWidget):
    valueChanged = pyqtSignal(int)
    lengthUnitChanged = pyqtSignal(LengthUnit)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(QHBoxLayout(self))
        self.data = dict()
        self.valueW = IntLineEdit(self)
        self.unitsW = QComboBox(self)

        self.populate()

        self.layout().addWidget(self.valueW)
        self.layout().addWidget(self.unitsW)

        self.valueW.valueChanged.connect(self.onValueChange)
        self.unitsW.activated.connect(self.onUnitActivate)
    def onValueChange(self, val):
        self.valueChanged.emit(val)
    def onUnitActivate(self, val):
        self.lengthUnitChanged.emit(self.data[val])
    def insertItem(self, idx, txt):
        self.unitsW.insertItem(idx, txt)
    def populate(self):
        idx = 0
        self.data[idx] = None
        self.insertItem(idx, unicode(""))
        idx += 1

        for d in QApplication.instance().lengthUnitModel.data:
            self.data[idx] = d
            self.insertItem(idx, QString(d.name))
            idx += 1
    def setValue(self, value, unit):
        self.valueW.setValue(value)
        for k, v in self.data.iteritems():
            if unit == v:
                self.unitsW.setCurrentIndex(k)
                return
