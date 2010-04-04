from RectItem import *

from LegendHeader import *

class LegendItemGroup(RectItem):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, title, profile):
        RectItem.__init__(self, parent, scene, rect, pos)
        self.headerFont = headerFont
        self.legendFont = legendFont
        self.profile = profile
        self.y = 0
        self.headerItm = LegendHeader(self, self.headerFont, QPointF(0, 0))
        self.headerItm.setText(title)
        self.y += self.headerItm.boundingRect().height()

