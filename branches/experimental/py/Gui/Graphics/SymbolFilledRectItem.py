from PyQt4.QtCore import *
from PyQt4.QtGui import *

from BrushFactory import *

class SymbolFilledRectItem(QGraphicsRectItem):
    def __init__(self, parent, scene, rect, pen, bed):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.setRect(rect)
        self.setPen(pen)
        self.bed = bed
    def createColRect(self, begin, end, colWidth, colNum, drawing):
        itm = QGraphicsRectItem(self, self.scene())
        fac = BrushFactory()
        brush = fac.fromDrawing(drawing)
        itm.setBrush(brush)
        itm.setPen(self.pen())
        itm.setRect(QRectF(0, 0, 
                           colWidth, self.rect().height() * (end - begin) / 100.0))
        itm.setPos(QPointF(colNum * colWidth, 
                           self.rect().height() - (self.rect().height() * end / 100)))
    def showSymbols(self, symbolMap):        
        cols = len(symbolMap)
        if cols < 1:
            return
        colWidth = self.rect().width() / cols
        col = 0
        for k, v in symbolMap.iteritems():
            self.createColRect(v[0], v[1], colWidth, col, k.drawing)
            col += 1
