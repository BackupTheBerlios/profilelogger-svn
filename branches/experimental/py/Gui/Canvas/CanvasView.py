from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CanvasView(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform | QPainter.HighQualityAntialiasing | QPainter.NonCosmeticDefaultPen)
    def onIntZoomChange(self, z):
        m = QMatrix()
        m.scale(1 + z/100.0, 1 + z/100.0)
        self.setMatrix(m)
