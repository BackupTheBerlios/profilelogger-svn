from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Model.Ellipsis import *

class EllipsisItem(QGraphicsEllipseItem):
    def __init__(self, ellipsis=None):
        QGraphicsEllipseItem.__init__(self)
        self.ellipsis = ellipsis
        self.updateFromData()
    def hasEllipsis(self):
        return self.ellipsis is not None
    def updateFromData(self):
        if not self.hasEllipsis():
            return
        self.setRect(self.ellipsis.makeRect())
        if self.ellipsis.hasPen():
            self.setPen(self.ellipsis.pen.getQPen())
        if self.ellipsis.hasBrush():
            self.setBrush(self.ellipsis.brush.getQBrush())
        self.setPos(self.ellipsis.makePosition())
