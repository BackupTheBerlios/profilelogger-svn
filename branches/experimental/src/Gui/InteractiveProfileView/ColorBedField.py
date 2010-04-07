from PatternInteractiveRectItem import *

class ColorBedField(PatternInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        PatternInteractiveRectItem.__init__(self, parent, scene, 
                                            rect, pos, 
                                            font, col, bed)
