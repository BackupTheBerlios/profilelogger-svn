from PyQt4.QtGui import *
from PyQt4.QtCore import *

from HeaderText import *

class HeaderItem(QGraphicsRectItem):
    def __init__(self, parent, scene, rect, pen, lbl, lblAngle):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.setRect(rect)
        self.setPen(pen)
        self.lbl = HeaderText(self, scene, QFont(), lbl, lblAngle)
        self.lbl.adjustSize()
        if lblAngle != 0:
            self.lbl.setPos(QPointF((self.rect().width() - self.lbl.boundingRect().height()) / 2, 
                                    self.rect().height()))
        else:
            self.lbl.setPos(QPointF((self.rect().width() - self.lbl.boundingRect().width()) / 2, 
                                    self.rect().height() - self.lbl.boundingRect().height()))
