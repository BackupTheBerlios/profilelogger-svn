from RectItem import *

class LegendDataItem(RectItem):
    def __init__(self, parent, scene, rect, pos, font, data):
        RectItem.__init__(self, parent, scene, rect, pos)
        self.font = font
        self.data = data
        self.maxY = 0
    def hasData(self):
        return self.data is not None
    def createDisplay(self):
        self.displayItm = QGraphicsRectItem(self, self.scene())
        self.displayItm.setRect(QRectF(0, 0, 
                                       self.rect().width() * 0.8, 
                                       self.rect().width() * 0.8))
        self.displayItm.setPen(Qt.blue)
        self.displayItm.setPos(QPointF(self.rect().width() * 0.2 / 2,
                                       self.rect().width() * 0.2 / 2))
        self.maxY += self.displayItm.pos().y() + self.displayItm.rect().height()
    def createIdDisplay(self):
        self.idItm = QGraphicsTextItem('%i' % self.data.id, self, self.scene())
        self.idItm.setFont(self.font)
        self.idItm.adjustSize()
        self.idItm.setPos(QPointF((self.rect().width() - self.idItm.boundingRect().width()) / 2, self.maxY))
        self.maxY += self.idItm.boundingRect().height()
    def createNameDisplay(self):
        self.nameItm = QGraphicsTextItem(unicode(self.data.name.replace(' ', '\n')), self, self.scene())
        self.nameItm.setFont(self.font)
        self.nameItm.adjustSize()
        self.nameItm.setPos(QPointF((self.rect().width() - self.nameItm.boundingRect().width()) / 2, self.maxY))
        self.maxY += self.idItm.boundingRect().height()
