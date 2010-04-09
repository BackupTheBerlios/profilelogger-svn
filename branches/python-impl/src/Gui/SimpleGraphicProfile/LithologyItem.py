from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class LithologyItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        self.drawLithologyPatterns()
    def drawLithologyPatterns(self):
        for l in self.bed.lithologies:
            if l.hasLithology():
                self.fillPercentRectWithSvgItem(l.begin, l.end, l.lithology.svgItem)
        
