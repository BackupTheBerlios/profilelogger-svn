from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class BeddingTypeItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        self.drawBeddingTypePatterns()
    def drawBeddingTypePatterns(self):
        for l in self.bed.beddingTypes:
            if l.hasBeddingType():
                self.fillPercentRectWithDrawing(l.begin, l.end, l.beddingType.drawing)
        
