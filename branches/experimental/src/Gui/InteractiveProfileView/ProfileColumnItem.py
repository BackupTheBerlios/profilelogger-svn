from InteractiveRectItem import *

from BedItem import *

class ProfileColumnItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, legendFont, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.legendFont = legendFont
        self.profile = profile
        self.maxY = 0
        self.drawBeds()
        self.setRect(QRectF(0, 0, self.rect().width(), self.maxY))
    def drawBeds(self):
        for bed in self.profile.beds:
            itm = BedItem(self, self.scene(),
                          QRectF(0, 0, self.rect().width(), bed.heightInPixel()),
                          QPointF(0, self.maxY),
                          self.legendFont, 
                          bed)
            self.maxY += itm.rect().height()
