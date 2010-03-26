from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class LithologicalUnitItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        self.drawLithologicalUnitPatterns()
    def drawLithologicalUnitPatterns(self):
        for l in self.bed.lithologicalUnits:
            if l.hasLithologicalUnit():
                self.fillPercentRectWithDrawing(l.begin, l.end, l.lithologicalUnit.drawing)
        
