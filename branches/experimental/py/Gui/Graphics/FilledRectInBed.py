from PyQt4.QtCore import *
from PyQt4.QtGui import *

from BrushFactory import *

class FilledRectInBed(QGraphicsRectItem):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.bed = bed
        self.setRect(rect)
        self.setPen(pen)
    def fillPercentRectWithDrawing(self, begin, end, drawing):
        itm = QGraphicsRectItem(self, self.scene())
        itm.setRect(QRectF(0, 0, 
                           self.rect().width(), 
                           self.rect().height() * (end - begin) / 100.0))
        itm.setPos(QPointF(0, 
                           self.rect().height() - (self.rect().height() * end / 100)))
        if drawing is not None:
            fac = BrushFactory()
            b = fac.fromDrawing(drawing)
            itm.setBrush(b)
