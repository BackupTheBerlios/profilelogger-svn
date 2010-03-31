from PyQt4.QtGui import *
from PyQt4.QtCore import *

class HeaderText(QGraphicsTextItem):
    def __init__(self, parent, scene, font, lbl, lblAngle):
        QGraphicsTextItem.__init__(self, lbl, parent)
        self.setFont(font)
        self.setRotation(lblAngle)
        self.adjustSize()
