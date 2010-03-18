from PyQt4.QtGui import *
from PyQt4.QtCore import *

class LineItem(QGraphicsLineItem):
    def __init__(self, parent, scene, color=Qt.black, line=None):
        QGraphicsLineItem.__init__(self, parent, scene)
        self.setPen(color)
        if line is not None:
            self.setLine(line)
