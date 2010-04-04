from InteractiveRectItem import *

from LithologyLegend import *

class LegendItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect)
        self.headerFont = headerFont
        self.legendFont = legendFont
        self.profile = profile
        self.y = 0
        self.lithologyL = LithologyLegend(self, 
                                          self.scene(),
                                          QRectF(0, 0, self.rect().width(), 0),
                                          QPointF(0, self.y),
                                          self.headerFont,
                                          self.legendFont,
                                          self.profile)
        self.setRect(QRectF(0, 0, self.rect().width(), self.y))
