from InteractiveRectItem import *

from Gui.SimpleGraphicProfile.BrushFactory import *

class PatternInteractiveRectItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, font, col, bed):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.bed = bed
        self.font = font
        self.col = col
        self.bed = bed
    def createRect(self, begin, end):
        self.rectItm = QGraphicsRectItem(self, self.scene())
        self.rectItm.setRect(QRectF(0, 0, 
                                    self.rect().width(), 
                                    self.rect().height() * (end - begin) / 100.0))
        self.rectItm.setPos(QPointF(0, 
                                    self.rect().height() - (self.rect().height() * end / 100)))
    def fillPercentRectWithSvgItem(self, begin, end, svgItem):
        self.createRect(begin, end)
        if svgItem is not None:
            fac = BrushFactory()
            b = fac.fromSvgItem(svgItem)
            self.rectItm.setBrush(b)
