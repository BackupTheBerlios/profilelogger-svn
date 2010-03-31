from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Model.StraightLine import *

class StraightLineItem(QGraphicsLineItem):
    def __init__(self, straightLine=None):
        QGraphicsLineItem.__init__(self)
        self.straightLine = straightLine
        self.updateFromData()
    def hasStraightLine(self):
        return self.straightLine is not None
    def updateFromData(self):
        if not self.hasStraightLine():
            return
        self.setLine(self.straightLine.makeLine())
        if self.straightLine.hasPen():
            self.setPen(self.straightLine.pen.getQPen())
