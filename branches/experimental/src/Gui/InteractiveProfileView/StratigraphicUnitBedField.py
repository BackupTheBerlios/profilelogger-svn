from PatternInteractiveRectItem import *

class StratigraphicUnitBedField(PatternInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        PatternInteractiveRectItem.__init__(self, parent, scene, 
                                            rect, pos, 
                                            font, col, bed)
