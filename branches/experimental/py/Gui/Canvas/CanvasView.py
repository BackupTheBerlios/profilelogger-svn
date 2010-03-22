from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CanvasView(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform | QPainter.HighQualityAntialiasing | QPainter.NonCosmeticDefaultPen)
