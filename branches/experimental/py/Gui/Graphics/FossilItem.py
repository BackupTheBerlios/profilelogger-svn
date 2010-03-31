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
        svgItems = dict()

        for f in self.bed.fossils:
            if f.fossil.hasSvgItem():
                svgItems[f.fossil] = [f.begin, f.end]
        self.showSymbols(svgItems)
