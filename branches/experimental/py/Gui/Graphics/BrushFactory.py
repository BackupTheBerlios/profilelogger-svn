from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Canvas.StraightLineItem import *
from Gui.Canvas.RectangleItem import *
from Gui.Canvas.EllipseItem import *
from Gui.Canvas.PolygonItem import *
from Gui.Canvas.PainterPathItem import *

class BrushFactory(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
    def fromDrawing(self, drawing, scalePixmapTo=None):
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
            s.addItem(PainterPathItem(p))
        pm = QPixmap(s.sceneRect().width(), s.sceneRect().height())
        pm.fill(Qt.white)
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
        finalPm = pm
        if scalePixmapTo is not None:
            finalPm = pm.scaled(scalePixmapTo, scalePixmapTo, Qt.KeepAspectRatio)
        brush.setTexture(finalPm)
        return brush
