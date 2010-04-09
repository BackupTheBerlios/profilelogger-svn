from PatternInteractiveRectItem import *

class FaciesBedField(PatternInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        PatternInteractiveRectItem.__init__(self, parent, scene, 
                                            rect, pos, 
                                            font, col, bed)
        for l in self.bed.facies:
            self.fillPercentRectWithSvgItem(l.begin, l.end, l.facies.svgItem)
