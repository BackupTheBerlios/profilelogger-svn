from PyQt4.QtGui import *
from PyQt4.QtCore import *

class RectItem(QGraphicsRectItem):
    def __init__(self, parent, scene, rect=None):
        QGraphicsRectItem.__init__(self, parent, scene)
        if rect is not None:
            self.setRect(rect)
