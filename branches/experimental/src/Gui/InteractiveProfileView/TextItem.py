from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSvg import *

class TextItem(QGraphicsTextItem):
    def __init__(self, parent, font=None, pos=None):
        QGraphicsTextItem.__init__(self, parent)
        if font is not None:
            self.setFont(font)
        self.adjustSize()
        if pos is not None:
            self.setPos(pos)
    def setText(self, txt):
        self.setPlainText(txt)
        self.adjustSize()
