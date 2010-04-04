from InteractiveRectItem import *

class ProfileHeaderItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.headerFont = headerFont
        self.legendFont = legendFont
        self.profile = profile
        self.setRect(QRectF(0, 0, self.rect().width(), 20))
