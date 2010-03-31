from PyQt4.QtGui import *
from PyQt4.QtCore import *

from SymbolFilledRectItem import *

class CustomSymbolItem(SymbolFilledRectItem):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        SymbolFilledRectItem.__init__(self, parent, scene, rect, pen, bed)
        self.setRect(rect)
        self.bed = bed
        self.showCustomSymbols()
    def showCustomSymbols(self):
        svgItems = dict()

        for f in self.bed.customSymbols:
            if f.customSymbol.hasSvgItem():
                svgItems[f.customSymbol] = [f.begin, f.end]
        self.showSymbols(svgItems)
