from NamedDescribedDataset import *

from PyQt4.QtCore import *

class BrushStyle(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None, qtEnumValue=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.qtEnumValue = qtEnumValue
        self.styles = {}
        self.styles[0] = Qt.NoBrush
        self.styles[1] = Qt.SolidPattern
        self.styles[2] = Qt.Dense1Pattern
        self.styles[3] = Qt.Dense2Pattern
        self.styles[4] = Qt.Dense3Pattern
        self.styles[5] = Qt.Dense4Pattern
        self.styles[6] = Qt.Dense5Pattern
        self.styles[7] = Qt.Dense6Pattern
        self.styles[8] = Qt.Dense7Pattern
        self.styles[9] = Qt.HorPattern
        self.styles[10] = Qt.VerPattern
        self.styles[11] = Qt.CrossPattern
        self.styles[12] = Qt.BDiagPattern
        self.styles[13] = Qt.FDiagPattern
        self.styles[14] = Qt.DiagCrossPattern
    def enumFromEnumValue(self):
        return self.styles[self.qtEnumValue]
