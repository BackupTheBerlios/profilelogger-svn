from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.Canvas.StraightLineItem import *
from Gui.Canvas.RectangleItem import *
from Gui.Canvas.EllipseItem import *
from Gui.Canvas.PolygonItem import *
from Gui.Canvas.PainterPathItem import *

class FilledRectInBed(QGraphicsRectItem):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.bed = bed
        self.setRect(rect)
        self.setPen(pen)
    def makeBrushFromDrawing(self, drawing):
        s = QGraphicsScene()
        for l in drawing.straightLines:
            s.addItem(StraightLineItem(l))
        for r in drawing.rectangles:
            s.addItem(RectangleItem(r))
        for e in drawing.ellipses:
            s.addItem(EllipseItem(e))
        for p in drawing.polygons:
            s.addItem(PolygonItem(p))
        for p in drawing.painterPaths:
            s.additem(PainterPathItem(p))
        pm = QPixmap(s.sceneRect().width(), s.sceneRect().height())
        pntr = QPainter()
        pntr.begin(pm)
        pntr.setRenderHints(QPainter.Antialiasing | 
                            QPainter.TextAntialiasing | 
                            QPainter.SmoothPixmapTransform | 
                            QPainter.HighQualityAntialiasing | 
                            QPainter.NonCosmeticDefaultPen)
        s.render(pntr)
        pntr.end()
        brush = QBrush()
        brush.setTexture(pm)
        return brush
    def fillPercentRectWithDrawing(self, begin, end, drawing):
        itm = QGraphicsRectItem(self, self.scene())
        itm.setRect(QRectF(0, 0, 
                           self.rect().width(), 
                           self.rect().height() * (end - begin) / 100.0))
        itm.setPos(QPointF(0, 
                           self.rect().height() - (self.rect().height() * end / 100)))
        if drawing is not None:
            itm.setBrush(self.makeBrushFromDrawing(drawing))
