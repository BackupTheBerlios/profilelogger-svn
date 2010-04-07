from SymbolInteractiveRectItem import *

class SedimentStructureBedField(SymbolInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        SymbolInteractiveRectItem.__init__(self, parent, scene, 
                                           rect, pos, 
                                           font, col, bed)
