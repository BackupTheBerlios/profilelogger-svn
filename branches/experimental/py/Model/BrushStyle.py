from NamedDescribedDataset import *

from PyQt4.QtCore import *

class BrushStyle(NamedDescribedDataset):
    styles = {}
    styles[0] = Qt.NoBrush
    styles[1] = Qt.SolidPattern
    styles[2] = Qt.Dense1Pattern
    styles[3] = Qt.Dense2Pattern
    styles[4] = Qt.Dense3Pattern
    styles[5] = Qt.Dense4Pattern
    styles[6] = Qt.Dense5Pattern
    styles[7] = Qt.Dense6Pattern
    styles[8] = Qt.Dense7Pattern
    styles[9] = Qt.HorPattern
    styles[10] = Qt.VerPattern
    styles[11] = Qt.CrossPattern
    styles[12] = Qt.BDiagPattern
    styles[13] = Qt.FDiagPattern
    styles[14] = Qt.DiagCrossPattern
    def __init__(self, id=None, name=None, description=None, qtEnumValue=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.qtEnumValue = qtEnumValue
    def enumFromEnumValue(self):
        return self.styles[self.qtEnumValue]
