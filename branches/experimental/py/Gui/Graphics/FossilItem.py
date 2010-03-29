from PyQt4.QtGui import *
from PyQt4.QtCore import *

from SymbolFilledRectItem import *

class FossilItem(SymbolFilledRectItem):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        SymbolFilledRectItem.__init__(self, parent, scene, rect, pen, bed)
        self.setRect(rect)
        self.setPen(pen)
        self.bed = bed
        self.showFossils()
    def showFossils(self):
        drawings = dict()

        for f in self.bed.fossils:
            if f.fossil.hasDrawing():
                drawings[f.fossil] = [f.begin, f.end]
        self.showSymbols(drawings)
