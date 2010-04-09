from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

class SymbolFactory(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
    def pixmapFromSvgItem(self, itm, scaleTo, aspectRatioStrategy=Qt.KeepAspectRatio):
        if itm.svgData is None:
            return None
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
        if aspectRatioStrategy == Qt.KeepAspectRatio:
            return pm.scaled(scaleTo, scaleTo, aspectRatioStrategy, Qt.SmoothTransformation)
        else:
            return pm.scaled(scaleTo, pm.height(), aspectRatioStrategy, Qt.SmoothTransformation)
