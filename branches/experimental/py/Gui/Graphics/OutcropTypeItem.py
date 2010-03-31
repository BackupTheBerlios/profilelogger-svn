from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class OutcropTypeItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        self.drawOutcropTypePatterns()
    def drawOutcropTypePatterns(self):
        for l in self.bed.outcropTypes:
            if l.hasOutcropType():
                self.fillPercentRectWithSvgItem(l.begin, l.end, l.outcropType.svgItem)
        
