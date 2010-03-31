from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

class SymbolFactory(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
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
