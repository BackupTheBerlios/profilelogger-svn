from PatternInteractiveRectItem import *

class TectonicUnitBedField(PatternInteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        PatternInteractiveRectItem.__init__(self, parent, scene, 
                                            rect, pos, 
                                            font, col, bed)
        for l in self.bed.tectonicUnits:
            self.fillPercentRectWithSvgItem(l.begin, l.end, l.tectonicUnit.svgItem)
