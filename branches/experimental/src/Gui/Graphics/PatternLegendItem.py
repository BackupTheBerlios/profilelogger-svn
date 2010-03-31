from LegendItem import *

from BrushFactory import *

class PatternLegendItem(LegendItem):
    def __init__(self, parent, scene, rect, pen, font, dataset):
        LegendItem.__init__(self, parent, scene, rect, pen, font, dataset)
        self.drawDatasetPattern()
        self.drawDatasetNumber()
        self.drawDatasetName()
    def drawDatasetPattern(self):
        w = self.rect().width() * 0.8
        self.patternItm = QGraphicsRectItem(self, self.scene())
        self.patternItm.setRect(QRectF(0, 0, w, w))
        self.patternItm.setPen(Qt.black)
        if self.dataset.hasSvgItem():
            f = BrushFactory()
            brush = f.fromSvgItem(self.dataset.svgItem)
            self.patternItm.setBrush(brush)

        self.patternItm.setPos(QPointF(self.rect().width() * 0.2 / 2,
                                       self.rect().width() * 0.2 / 2))
    def drawDatasetNumber(self):
        self.idItm = QGraphicsTextItem(QString("%1").arg(self.dataset.id), self, self.scene())
        self.idItm.setFont(self.font)
        self.idItm.adjustSize()
        self.idItm.setPos(QPointF((self.rect().width() - self.idItm.boundingRect().width()) / 2.0,
                                  self.patternItm.pos().y() + self.patternItm.rect().height()))
    def drawDatasetName(self):
        self.nameItm = QGraphicsTextItem(self.dataset.name.replace(' ', '\n'), self, self.scene())
        self.nameItm.setFont(self.font)
        self.nameItm.adjustSize()
        self.nameItm.setPos(QPointF((self.rect().width() - self.nameItm.boundingRect().width()) / 2.0,
                                    self.idItm.pos().y() + self.idItm.boundingRect().height()))
