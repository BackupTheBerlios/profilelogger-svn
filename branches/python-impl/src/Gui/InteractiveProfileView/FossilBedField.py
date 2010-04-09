from SymbolInteractiveRectItem import *

class FossilBedField(SymbolInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        SymbolInteractiveRectItem.__init__(self, parent, scene, 
                                           rect, pos, 
                                           font, col, bed)
        self.showFossils()    
    def showFossils(self):
        svgItems = dict()

        for f in self.bed.fossils:
            if f.fossil.hasSvgItem():
                svgItems[f.fossil] = [f.begin, f.end]
        self.showSymbols(svgItems)
