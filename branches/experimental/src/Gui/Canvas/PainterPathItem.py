from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Model.PainterPath import *

class PainterPathItem(QGraphicsPathItem):
    def __init__(self, painterPath=None):
        QGraphicsPathItem.__init__(self)
        self.painterPath = painterPath
        self.updateFromData()
    def hasPainterPath(self):
        return self.painterPath is not None
    def updateFromData(self):
        if not self.hasPainterPath():
            return
        self.setPath(self.painterPath.makePainterPath())
        if self.painterPath.hasPen():
            self.setPen(self.painterPath.pen.getQPen())
        if self.painterPath.hasBrush():
            self.setBrush(self.painterPath.brush.getQBrush())
        self.setPos(self.painterPath.makePosition())
