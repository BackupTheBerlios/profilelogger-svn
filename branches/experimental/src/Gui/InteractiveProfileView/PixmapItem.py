from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

from Gui.SimpleGraphicProfile.SymbolFactory import *

class PixmapItem(QGraphicsPixmapItem):
    def __init__(self, parent, scene, maxSize, data):
        QGraphicsPixmapItem.__init__(self, parent)
        f = SymbolFactory(self.scene())
        self.setPixmap(f.pixmapFromSvgItem(data, maxSize))
