from LegendDataItem import *

from PixmapItem import *

class SymbolLegendItem(LegendDataItem):
    def __init__(self, parent, scene, rect, pos, font, data):
        LegendDataItem.__init__(self, parent, scene, rect, pos, font, data)
        self.createDisplay()
        self.createIdDisplay()
        self.createNameDisplay()
        self.fillDisplay()
        self.displayItm.setPen(QPen(Qt.NoPen))
    def fillDisplay(self):
        if not self.hasData():
            return
        if self.data.hasSvgItem():
            pmItm = PixmapItem(self.displayItm, 
                               self.scene(), 
                               self.displayItm.rect().width(),
                               self.data.svgItem)
            pmItm.setPos(QPointF((self.displayItm.rect().width() - pmItm.boundingRect().width()) / 2,
                                 (self.displayItm.rect().height() - pmItm.boundingRect().height()) / 2))
