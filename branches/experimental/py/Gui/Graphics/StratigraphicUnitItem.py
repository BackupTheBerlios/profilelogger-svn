from PyQt4.QtGui import *
from PyQt4.QtCore import *

class StratigraphicUnitItem(QGraphicsRectItem):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.setRect(rect)
        self.setPen(pen)
        
