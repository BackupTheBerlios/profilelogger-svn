from InteractiveRectItem import *

from LegendItem import *

class ProfileItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.profile = profile
        self.headerFont = QFont()
        self.headerFont.setPointSize(12)
        self.legendFont = QFont()
        self.legendFont.setPointSize(10)
        self.y = 0
        self.drawLegend()
        self.setRect(QRectF(0, 0, self.rect().width(), self.y))
    def drawLegend(self):
        self.legendItm = LegendItem(self, self.scene(),
                                    QRectF(0, 0, self.rect().width(), 20),
                                    QPoint(0, 0),
                                    self.headerFont,
                                    self.legendFont,
                                    self.profile)
        self.legendItm.setPen(QPen(Qt.black))
        self.y += self.legendItm.rect().height()
    def drawProfileHeader(self):
        pass
    def drawProfile(self):
        pass
