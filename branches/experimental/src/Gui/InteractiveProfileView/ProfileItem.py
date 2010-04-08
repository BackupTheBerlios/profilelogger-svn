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
    def editBed(self, bed):
        self.profileItm.editBed(bed)
    def createBedAtTop(self):
        self.profileItm.createBedOnTop()
    def splitBed(self, bed):
        pass
    def deleteBed(self, bed):
        pass
    def deleteBedsAbove(self, bed):
        pass
    def deleteBedsBelow(self, bed):
        pass
    def mergeWithAbove(self, bed):
        pass
    def mergeWithBelow(self, bed):
        pass
    def createBedAtBottom(self):
        self.profileItm.createBedAtBottom()
    def createBedAbove(self, bed):
        pass
    def createBedBelow(self, bed):
        pass
    def renumberFromBase(self):
        pass
    def renumberFromTop(self):
        pass
    def splitProfileAbove(self, bed):
        pass
    def splitProfileBelow(self, bed):
        pass
    def insertProfileAbove(self, bed):
        pass
    def insertProfileBelow(self, bed):
        pass
