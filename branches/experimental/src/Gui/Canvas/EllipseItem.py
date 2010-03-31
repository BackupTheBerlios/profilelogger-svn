from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Model.Ellipse import *

class EllipseItem(QGraphicsEllipseItem):
    def __init__(self, ellipse=None):
        QGraphicsEllipseItem.__init__(self)
        self.ellipse = ellipse
        self.updateFromData()
    def hasEllipsis(self):
        return self.ellipse is not None
    def updateFromData(self):
        if not self.hasEllipsis():
            return
        self.setRect(self.ellipse.makeRect())
        if self.ellipse.hasPen():
            self.setPen(self.ellipse.pen.getQPen())
        if self.ellipse.hasBrush():
            self.setBrush(self.ellipse.brush.getQBrush())
        self.setPos(self.ellipse.makePosition())
