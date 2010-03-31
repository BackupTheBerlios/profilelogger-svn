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
    def createRect(self, begin, end):
        self.rectItm = QGraphicsRectItem(self, self.scene())
        self.rectItm.setRect(QRectF(0, 0, 
                                    self.rect().width(), 
                                    self.rect().height() * (end - begin) / 100.0))
        self.rectItm.setPos(QPointF(0, 
                                    self.rect().height() - (self.rect().height() * end / 100)))
    def fillPercentRectWithDrawing(self, begin, end, drawing):
        self.createRect(begin, end)
        if drawing is not None:
            fac = BrushFactory()
            b = fac.fromDrawing(drawing)
            self.rectItm.setBrush(b)
    def fillPercentRectWithSvgItem(self, begin, end, svgItem):
        self.createRect(begin, end)
        if svgItem is not None:
            fac = BrushFactory()
            b = fac.fromSvgItem(svgItem)
            self.rectItm.setBrush(b)
