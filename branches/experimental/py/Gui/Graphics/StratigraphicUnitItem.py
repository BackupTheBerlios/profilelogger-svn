from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class StratigraphicUnitItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        self.drawStratigraphicUnitPatterns()
    def drawStratigraphicUnitPatterns(self):
        for l in self.bed.stratigraphicUnits:
            if l.hasStratigraphicUnit():
                self.fillPercentRectWithDrawing(l.begin, l.end, l.stratigraphicUnit.drawing)
        
