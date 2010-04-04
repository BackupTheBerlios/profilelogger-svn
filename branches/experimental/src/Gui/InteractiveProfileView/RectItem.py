from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSvg import *

class RectItem(QGraphicsRectItem):
    def __init__(self, parent, scene, rect=None, pos=None):
        QGraphicsRectItem.__init__(self, parent, scene)
        if rect is not None:
            self.setRect(rect)
        if pos is not None:
            self.setPos(pos)
