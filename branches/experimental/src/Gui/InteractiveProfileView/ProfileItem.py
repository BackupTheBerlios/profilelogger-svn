from InteractiveRectItem import *

from LegendItem import *
from ProfileHeaderItem import *
from ProfileColumnItem import *

class ProfileItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.profile = profile
        self.headerFont = QFont()
        self.headerFont.setPointSize(12)
        self.legendFont = QFont()
        self.legendFont.setPointSize(10)
        self.maxY = 0
        self.spacing = 10
        self.drawLegend()
        self.drawProfileHeader()
        self.drawProfile()
        self.setRect(QRectF(0, 0, self.profile.displayWidth(), self.maxY))
    def drawLegend(self):
        self.legendItm = LegendItem(self, self.scene(),
                                    QRectF(0, 0, self.profile.displayWidth(), 0),
                                    QPoint(0, self.maxY),
                                    self.headerFont,
                                    self.legendFont,
                                    self.profile)
        self.maxY += self.legendItm.rect().height()
    def drawProfileHeader(self):
        self.headerItm = ProfileHeaderItem(self, self.scene(),
                                           QRectF(0, 0, self.profile.displayWidth(), 0),
                                           QPointF(0, self.maxY + self.spacing),
                                           self.headerFont,
                                           self.legendFont,
                                           self.profile)
        self.maxY += self.headerItm.rect().height() + self.spacing
    def drawProfile(self):
        self.profileItm = ProfileColumnItem(self, self.scene(),
                                            QRectF(0, 0, self.profile.displayWidth(), 0),
                                            QPointF(0, self.maxY),
                                            self.legendFont,
                                            self.profile)
        self.maxY += self.profileItm.rect().height()
