from PyQt4.QtCore import *
from PyQt4.QtGui import *

class GrainSizeBox(QGraphicsRectItem):
    def __init__(self, parent, scene,
                 grainSizeType,
                 rect, pos, pen):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.setRect(rect)
        self.setPos(pos)
        self.setPen(pen)
        self.f = QFont()
        self.f.setPointSize(9)
        self.grainSizeType = grainSizeType.grainSizeType
        self.drawItems()
    def drawItems(self):
        for gs in self.grainSizeType.grainSizes:
            self.drawLabelledTic(gs.shortName, self.rect().width() * gs.percentFromMinimum / 100)
        itm = QGraphicsTextItem(unicode(self.grainSizeType.name), self)
        itm.setFont(self.f)
        itm.adjustSize()
        itm.setPos(QPointF((self.rect().width() - itm.boundingRect().width()) / 2, 
                           0))

    def drawLabelledTic(self, txt, x, ticLengthFactor=10):
        self.drawTic(x, ticLengthFactor)
        self.drawLabel(txt, x, ticLengthFactor)
    def drawLabel(self, txt, x, ticLengthFactor):
        itm = QGraphicsTextItem(unicode(txt), self)
        itm.rotate(-90)
        itm.setFont(self.f)
        itm.adjustSize()
        itm.setPos(QPointF(x - itm.boundingRect().height() / 2, 
                           self.rect().height() - self.rect().height() / ticLengthFactor))
    def drawTic(self, x, ticLengthFactor):
        l = QGraphicsLineItem(self)
        l.setLine(QLineF(x, self.rect().height(), x, self.rect().height() - self.rect().height() / ticLengthFactor))
        l.setPen(self.pen())
