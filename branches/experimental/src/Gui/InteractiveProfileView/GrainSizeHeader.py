from HeaderItem import *

from GrainSizeBox import *
class GrainSizeHeader(HeaderItem):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, textAngle):
        HeaderItem.__init__(self, parent, scene, rect, pos, font, profileColumn, textAngle)
        self.grainSizeTypesInProfile = parent.profile.grainSizeTypes
        self.drawGrainSizeLegends()
    def drawGrainSizeLegends(self):
        if len(self.grainSizeTypesInProfile) < 1:
            return
        y = self.rect().height()
        itemHeight = y / len(self.grainSizeTypesInProfile)

        for gst in self.grainSizeTypesInProfile:
            box = GrainSizeBox(self, self.scene(),
                               QRectF(0, 0, self.rect().width(), itemHeight),
                               QPointF(0, y - itemHeight),
                               gst)
            y -= itemHeight
