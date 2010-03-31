from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Model.Polygon import *

class PolygonItem(QGraphicsPolygonItem):
    def __init__(self, polygon=None):
        QGraphicsPolygonItem.__init__(self)
        self.polygon = polygon
        self.updateFromData()
    def hasPolygon(self):
        return self.polygon is not None
    def updateFromData(self):
        if not self.hasPolygon():
            return
        self.setPolygon(self.polygon.makePolygon())
        if self.polygon.hasPen():
            self.setPen(self.polygon.pen.getQPen())
        if self.polygon.hasBrush():
            self.setBrush(self.polygon.brush.getQBrush())
        self.setPos(self.polygon.makePosition())
