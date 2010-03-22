from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EllipseItem(QGraphicsEllipseItem):
    def __init__(self, parent, scene, rect=None):
        QGraphicsEllipseItem.__init__(self, parent, scene)
        if rect is not None:
            self.setRect(rect)
