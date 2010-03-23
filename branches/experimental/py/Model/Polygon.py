from Dataset import Dataset

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Polygon(Dataset):
    def __init__(self, id=None, drawing=None,
                 posX=0, posY=0, 
                 polygonPoints = [],
                 pen=None, brush=None):
        Dataset.__init__(self, id)
        self.drawing = drawing
        self.posX = posX
        self.posY = posY
        self.polygonPoints = polygonPoints
        self.pen = pen
        self.brush = brush
    def hasPen(self):
        return self.pen is not None
    def hasBrush(self):
        return self.brush is not None
    def makePosition(self):
        return QPointF(self.posX, self.posY)
    def makePolygon(self):
        ret = QPolygonF()
        for p in self.polygonPoints:
            ret.append(QPointF(p.toPoint()))
        return ret
