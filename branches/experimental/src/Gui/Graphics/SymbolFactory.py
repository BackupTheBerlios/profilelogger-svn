from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

from Gui.Canvas.StraightLineItem import *
from Gui.Canvas.RectangleItem import *
from Gui.Canvas.EllipseItem import *
from Gui.Canvas.PolygonItem import *
from Gui.Canvas.PainterPathItem import *

class SymbolFactory(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
    def pixmapFromDrawing(self, drawing, scalePixmapTo=None):
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

        if scalePixmapTo is not None:
            return pm.scaled(scalePixmapTo, scalePixmapTo, Qt.KeepAspectRatio)
        else:
            return pm
    def pixmapFromSvgItem(self, itm, scaleTo):
        xmlStrm = QXmlStreamReader(itm.svgData)
        gen = QSvgRenderer()
        gen.load(xmlStrm)
        pm = QPixmap(gen.defaultSize())
        pm.fill(Qt.white)
        pntr = QPainter()
        pntr.begin(pm)
        pntr.setRenderHints(QPainter.Antialiasing | 
                            QPainter.TextAntialiasing | 
                            QPainter.SmoothPixmapTransform | 
                            QPainter.HighQualityAntialiasing | 
                            QPainter.NonCosmeticDefaultPen)
        gen.render(pntr)
        pntr.end()
        return pm.scaled(scaleTo, scaleTo, Qt.KeepAspectRatio, Qt.SmoothTransformation)
