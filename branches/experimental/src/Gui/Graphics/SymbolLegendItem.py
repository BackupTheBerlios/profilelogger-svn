from LegendItem import *

from SymbolFactory import *

class SymbolLegendItem(LegendItem):
    def __init__(self, parent, scene, rect, pen, font, dataset):
        LegendItem.__init__(self, parent, scene, rect, pen, font, dataset)
        self.drawDatasetSymbol()
        self.drawDatasetNumber()
        self.drawDatasetName()
    def drawDatasetSymbol(self):
        w = self.rect().width() * 0.8
        self.symbolItm = QGraphicsRectItem(self, self.scene())
        self.symbolItm.setRect(QRectF(0, 0, w, w))
        self.symbolItm.setPen(QPen(Qt.NoPen))
        if self.dataset.hasSvgItem():
            f = SymbolFactory()
            pm = f.pixmapFromSvgItem(self.dataset.svgItem, w)
            pmItm = QGraphicsPixmapItem(self.symbolItm, self.scene())
            pmItm.setPixmap(pm)
            pmItm.setPos(QPointF((self.symbolItm.rect().width() - pmItm.boundingRect().width()) / 2, 
                                 (self.symbolItm.rect().height() - pmItm.boundingRect().height()) / 2))
        self.symbolItm.setPos(QPointF(self.rect().width() * 0.2 / 2,
                                       self.rect().width() * 0.2 / 2))
    def drawDatasetNumber(self):
        self.idItm = QGraphicsTextItem(QString("%1").arg(self.dataset.id), self, self.scene())
        self.idItm.setFont(self.font)
        self.idItm.adjustSize()
        self.idItm.setPos(QPointF((self.rect().width() - self.idItm.boundingRect().width()) / 2.0,
                                  self.symbolItm.pos().y() + self.symbolItm.rect().height()))
    def drawDatasetName(self):
        self.nameItm = QGraphicsTextItem(self.dataset.name.replace(' ', '\n'), self, self.scene())
        self.nameItm.setFont(self.font)
        self.nameItm.adjustSize()
        self.nameItm.setPos(QPointF((self.rect().width() - self.nameItm.boundingRect().width()) / 2.0,
                                    self.idItm.pos().y() + self.idItm.boundingRect().height()))
