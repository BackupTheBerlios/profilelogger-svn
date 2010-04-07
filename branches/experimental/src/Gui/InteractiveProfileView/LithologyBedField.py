from PatternInteractiveRectItem import *

class LithologyBedField(PatternInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        PatternInteractiveRectItem.__init__(self, parent, scene, 
                                            rect, pos, 
                                            font, col, bed)
        for l in self.bed.lithologies:
            self.fillPercentRectWithSvgItem(l.begin, l.end, l.lithology.svgItem)
