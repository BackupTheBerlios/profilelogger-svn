from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class TectonicUnitItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        self.drawTectonicUnitPatterns()
    def drawTectonicUnitPatterns(self):
        for l in self.bed.tectonicUnits:
            if l.hasTectonicUnit():
                self.fillPercentRectWithDrawing(l.begin, l.end, l.tectonicUnit.drawing)
        
