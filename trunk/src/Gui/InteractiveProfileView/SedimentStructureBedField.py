from SymbolInteractiveRectItem import *

class SedimentStructureBedField(SymbolInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        SymbolInteractiveRectItem.__init__(self, parent, scene, 
                                           rect, pos, 
                                           font, col, bed)
        self.showSedimentStructures()
    def showSedimentStructures(self):
        svgItems = dict()

        for f in self.bed.sedimentStructures:
            if f.sedimentStructure.hasSvgItem():
                svgItems[f.sedimentStructure] = [f.begin, f.end]
        self.showSymbols(svgItems)
