from RectItem import *

from LegendHeader import *

class LegendItemGroup(RectItem):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, title, profile, itemClass):
        RectItem.__init__(self, parent, scene, rect, pos)
        self.headerFont = headerFont
        self.legendFont = legendFont
        self.profile = profile
        self.itemClass = itemClass
        self.maxY = 0
        self.headerItm = LegendHeader(self, self.headerFont, QPointF(0, 0))
        self.headerItm.setText(title)
        self.maxY += self.headerItm.boundingRect().height()
    def createItemWidth(self):
        return self.rect().width() / self.profile.colsInLegend
    def createItemHeight(self):
        return self.createItemWidth() * 1.5
    def createDisplayRect(self):
        return QRectF(0, 0, self.createItemWidth(), self.createItemHeight())
    def createItems(self, items):
        col = 0
        for i in items:
            itm = self.itemClass(self, self.scene(),
                                 self.createDisplayRect(),
                                 QPointF(self.createItemWidth() * col, self.maxY),
                                 self.legendFont,
                                 i)
            col += 1
            if col == self.profile.colsInLegend:
                col = 0
                self.maxY += self.createItemHeight()
        self.maxY += self.createItemHeight()
        w = self.rect().width()        
        self.setRect(QRectF(0, 0, w, self.maxY))
