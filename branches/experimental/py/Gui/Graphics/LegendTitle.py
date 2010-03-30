from PyQt4.QtGui import *
from PyQt4.QtCore import *

class LegendTitle(QGraphicsTextItem):
    def __init__(self, parent, scene, font, lbl):
        QGraphicsTextItem.__init__(self, lbl, parent)
        self.setFont(font)
        self.adjustSize()
