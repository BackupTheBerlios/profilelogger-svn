from HeaderItem import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from GrainSizeBox import *

class GrainSizeHeaderItem(HeaderItem):
    def __init__(self, parent, scene, rect, pen):
        HeaderItem.__init__(self, parent, scene, rect, pen, None, 0)
        self.grainSizeTypesInProfile = parent.profile.grainSizeTypes
        self.drawGrainSizeLegends()
    def drawGrainSizeLegends(self):
        y = self.rect().height()
        itemHeight = y / len(self.grainSizeTypesInProfile)

        for gst in self.grainSizeTypesInProfile:
            box = GrainSizeBox(self, self.scene(),
                               gst,
                               QRectF(0, 0, self.rect().width(), itemHeight),
                               QPointF(0, y - itemHeight),
                               self.pen())
            y -= itemHeight
