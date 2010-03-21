from NamedDescribedDataset import *

from PyQt4.QtCore import *

class PenJoinStyle(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None, qtEnumValue=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.qtEnumValue = qtEnumValue
        self.styles = {}
        self.styles[0x00] = Qt.MiterJoin
        self.styles[0x40] = Qt.BevelJoin
        self.styles[0x80] = Qt.RoundJoin
        self.styles[0x100] = Qt.SvgMiterJoin
    def enumFromEnumValue(self):
        return self.styles[self.qtEnumValue]
