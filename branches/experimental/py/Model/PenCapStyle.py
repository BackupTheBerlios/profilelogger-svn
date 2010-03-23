from NamedDescribedDataset import *

from PyQt4.QtCore import *

class PenCapStyle(NamedDescribedDataset):
    styles = {}
    styles[0x00] = Qt.FlatCap
    styles[0x10] = Qt.SquareCap
    styles[0x20] = Qt.RoundCap
    def __init__(self, id=None, name=None, description=None, qtEnumValue=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.qtEnumValue = qtEnumValue
    def enumFromEnumValue(self):
        return self.styles[self.qtEnumValue]
