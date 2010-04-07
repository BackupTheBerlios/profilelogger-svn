from PatternInteractiveRectItem import *

class OutcropTypeBedField(PatternInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        PatternInteractiveRectItem.__init__(self, parent, scene, 
                                            rect, pos, 
                                            font, col, bed)
        for l in self.bed.outcropTypes:
            self.fillPercentRectWithSvgItem(l.begin, l.end, l.outcropType.svgItem)
