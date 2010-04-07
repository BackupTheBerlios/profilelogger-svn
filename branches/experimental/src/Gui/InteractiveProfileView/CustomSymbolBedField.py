from SymbolInteractiveRectItem import *

class CustomSymbolBedField(SymbolInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        SymbolInteractiveRectItem.__init__(self, parent, scene, 
                                           rect, pos, 
                                           font, col, bed)
    def showCustomSymbols(self):
        svgItems = dict()

        for f in self.bed.customSymbols:
            if f.customSymbol.hasSvgItem():
                svgItems[f.customSymbol] = [f.begin, f.end]
        self.showSymbols(svgItems)
