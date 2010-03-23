from NamedDescribedDataset import *

from PyQt4.QtCore import *

class PenStyle(NamedDescribedDataset):
    styles = {}
    styles[0] = Qt.NoPen
    styles[1] = Qt.SolidLine
    styles[2] = Qt.DashLine
    styles[3] = Qt.DotLine
    styles[4] = Qt.DashDotLine
    styles[5] = Qt.DashDotDotLine
    def __init__(self, id=None, name=None, description=None, qtEnumValue=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.qtEnumValue = qtEnumValue
    def enumFromEnumValue(self):
        return self.styles[self.qtEnumValue]
