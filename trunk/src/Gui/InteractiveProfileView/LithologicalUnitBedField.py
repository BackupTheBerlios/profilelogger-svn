from PatternInteractiveRectItem import *

class LithologicalUnitBedField(PatternInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        PatternInteractiveRectItem.__init__(self, parent, scene, 
                                            rect, pos, 
                                            font, col, bed)
        for l in self.bed.lithologicalUnits:
            self.fillPercentRectWithSvgItem(l.begin, l.end, l.lithologicalUnit.svgItem)
