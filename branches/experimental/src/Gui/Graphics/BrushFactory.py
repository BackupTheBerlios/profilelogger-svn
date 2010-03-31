from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

class BrushFactory(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
    def fromSvgItem(self, itm, scaleTo=None):
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
        if scaleTo is not None:
            return QBrush(pm.scaled(scaleTo, scaleTo, 
                                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
        return QBrush(pm)
