from PyQt4.QtGui import *
from PyQt4.QtCore import *

from SymbolFilledRectItem import *

class SedimentStructureItem(SymbolFilledRectItem):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        SymbolFilledRectItem.__init__(self, parent, scene, rect, pen, bed)
        self.setRect(rect)
        self.setPen(pen)
        self.bed = bed
        self.showSedimentStructures()
    def showSedimentStructures(self):
        svgItems = dict()

        for f in self.bed.sedimentStructures:
            if f.sedimentStructure.hasSvgItem():
                svgItems[f.sedimentStructure] = [f.begin, f.end]
        self.showSymbols(svgItems)
