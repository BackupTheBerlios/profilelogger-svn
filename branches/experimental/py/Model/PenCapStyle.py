from NamedDescribedDataset import *

from PyQt4.QtCore import *

class PenCapStyle(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None, qtEnumValue=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.qtEnumValue = qtEnumValue
        self.styles = {}
        self.styles[0x00] = Qt.FlatCap
        self.styles[0x10] = Qt.SquareCap
        self.styles[0x20] = Qt.RoundCap
    def enumFromEnumValue(self):
        return self.styles[self.qtEnumValue]
