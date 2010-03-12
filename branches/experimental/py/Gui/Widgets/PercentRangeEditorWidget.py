from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PercentEditorWidget import *

class PercentRangeEditorWidget(QWidget):
    beginValueChanged = pyqtSignal(int)
    endValueChanged = pyqtSignal(int)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setLayout(QHBoxLayout(self))
        self.beginW = PercentEditorWidget(self)
        self.endW = PercentEditorWidget(self)
        self.layout().addWidget(self.beginW)
        self.layout().addWidget(QLabel(self.tr("-"), self))
        self.layout().addWidget(self.endW)
        self.beginW.valueChanged.connect(self.onBeginChange)
        self.endW.valueChanged.connect(self.onEndChange)
    def onBeginChange(self, v):
        self.beginValueChanged.emit(v)
    def onEndChange(self, v):
        self.endValueChanged.emit(v)
    def setValues(self, begin, end):
        self.beginW.setValue(begin)
        self.endW.setValue(end)
