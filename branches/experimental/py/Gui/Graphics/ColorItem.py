from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class ColorItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        self.drawColorPatterns()
    def drawColorPatterns(self):
        for l in self.bed.colors:
            if l.hasColor():
                self.fillPercentRectWithDrawing(l.begin, l.end, l.color.drawing)
        
