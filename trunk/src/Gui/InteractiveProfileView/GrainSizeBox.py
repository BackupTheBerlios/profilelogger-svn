from InteractiveRectItem import *
from TextItem import *

class GrainSizeBox(InteractiveRectItem):
    def __init__(self, parent, scene,
                 rect, pos, grainSizeType):
        InteractiveRectItem.__init__(self, parent, scene)
        self.setRect(rect)
        self.setPos(pos)
        self.f = QFont()
        self.f.setPointSize(9)
        self.grainSizeType = grainSizeType.grainSizeType
        self.drawItems()
    def drawItems(self):
        for gs in self.grainSizeType.grainSizes:
            self.drawLabelledTic(gs.shortName, self.rect().width() * gs.percentFromMinimum / 100)
        itm = TextItem(self, self.f)
        itm.setText(unicode(self.grainSizeType.name))
        itm.adjustSize()
        itm.setPos(QPointF((self.rect().width() - itm.boundingRect().width()) / 2, 
                           0))

    def drawLabelledTic(self, txt, x, ticLengthFactor=10):
        self.drawTic(x, ticLengthFactor)
        self.drawLabel(txt, x, ticLengthFactor)
    def drawLabel(self, txt, x, ticLengthFactor):
        itm = TextItem(self, self.f)
        itm.setText(unicode(txt))
        itm.rotate(-90)
        itm.adjustSize()
        itm.setPos(QPointF(x - itm.boundingRect().height() / 2, 
                           self.rect().height() - self.rect().height() / ticLengthFactor))
    def drawTic(self, x, ticLengthFactor):
        l = QGraphicsLineItem(self)
        l.setLine(QLineF(x, self.rect().height(), x, self.rect().height() - self.rect().height() / ticLengthFactor))
        l.setPen(self.pen())
