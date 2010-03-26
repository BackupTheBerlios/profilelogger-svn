from PyQt4.QtGui import *
from PyQt4.QtCore import *

from BedItem import *

class SimpleProfile(QGraphicsRectItem):
    def __init__(self, parent, scene, 
                 profile, 
                 rect, pos, pen, 
                 columnWidths, columnSequence):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.profile = profile
        self.columnWidths = columnWidths
        self.columnSequence = columnSequence
        self.headerItems = dict()
        self.setRect(rect)
        self.setPos(pos)
        self.setPen(pen)
        self.drawBeds()
    def drawBeds(self):
        y = self.rect().height()
        for b in self.profile.beds:
            y -= b.heightInMillimetres()
            BedItem(self, self.scene(), b,
                    QRectF(0, 0, self.rect().width(), b.heightInMillimetres()),
                    QPointF(0, y),
                    QPen(Qt.red),
                    self.columnWidths, self.columnSequence)
