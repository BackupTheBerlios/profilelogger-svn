from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class FaciesItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        self.drawFaciesPatterns()
    def drawFaciesPatterns(self):
        for l in self.bed.facies:
            if l.hasFacies():
                self.fillPercentRectWithSvgItem(l.begin, l.end, l.facies.svgItem)
        
