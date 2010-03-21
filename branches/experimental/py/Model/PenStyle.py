from NamedDescribedDataset import *

from PyQt4.QtCore import *

class PenStyle(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None, qtEnumValue=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.qtEnumValue = qtEnumValue
        self.styles = {}
        self.styles[0] = Qt.NoPen
        self.styles[1] = Qt.SolidLine
        self.styles[2] = Qt.DashLine
        self.styles[3] = Qt.DotLine
        self.styles[4] = Qt.DashDotLine
        self.styles[5] = Qt.DashDotDotLine
    def enumFromEnumValue(self):
        return self.styles[self.qtEnumValue]
