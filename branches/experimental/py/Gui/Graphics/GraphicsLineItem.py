from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GraphicsLineItem(QGraphicsLineItem):
    def __init__(self, parent, scene, startPoint, endPoint):
        QGraphicsLineItem.__init__(self, parent, scene)
        self.setLine(QLineF(startPoint, endPoint))
