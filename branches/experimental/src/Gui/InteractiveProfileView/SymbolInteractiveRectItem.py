from InteractiveRectItem import *

class SymbolInteractiveRectItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.bed = bed
        self.font = font
        self.col = col
        self.bed = bed
