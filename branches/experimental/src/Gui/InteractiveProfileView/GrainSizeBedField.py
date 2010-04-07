from InteractiveRectItem import *

class GrainSizeBedField(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.bed = bed
        self.font = font
        self.col = col
        self.bed = bed
