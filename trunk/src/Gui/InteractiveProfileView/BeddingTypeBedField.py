from PatternInteractiveRectItem import *

class BeddingTypeBedField(PatternInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        PatternInteractiveRectItem.__init__(self, parent, scene, 
                                            rect, pos, 
                                            font, col, bed)
        for l in self.bed.beddingTypes:
            self.fillPercentRectWithSvgItem(l.begin, l.end, l.beddingType.svgItem)
