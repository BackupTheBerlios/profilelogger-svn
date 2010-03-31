from NamedDescribedDataset import *

from PyQt4.QtCore import *

class PenJoinStyle(NamedDescribedDataset):
    styles = {}
    styles[0x00] = Qt.MiterJoin
    styles[0x40] = Qt.BevelJoin
    styles[0x80] = Qt.RoundJoin
    styles[0x100] = Qt.SvgMiterJoin
    def __init__(self, id=None, name=None, description=None, qtEnumValue=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.qtEnumValue = qtEnumValue
    def enumFromEnumValue(self):
        return self.styles[self.qtEnumValue]
