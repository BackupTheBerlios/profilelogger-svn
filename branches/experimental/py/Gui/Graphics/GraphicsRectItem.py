from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GraphicsRectItem(QGraphicsRectItem):
    def __init__(self, parent, scene):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.defaultPen = QPen(Qt.black)
        self.setPen(self.defaultPen)
