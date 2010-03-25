from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SimpleProfileHeader import *

class SimpleProfileModel(QGraphicsScene):
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.profile = None
        self.totalWidth=1000
        self.graphicPen = QPen(Qt.black)
        self.graphicPen.setStyle(Qt.SolidLine)
        self.graphicPen.setCapStyle(Qt.RoundCap)
        self.graphicPen.setJoinStyle(Qt.RoundJoin)
    def setProfile(self, profile):
        self.profile = profile
        self.updateItems()
    def updateItems(self):
        self.clear()
        self.updateLegend()
        self.updateHeader()
        self.updateProfile()
    def updateLegend(self):
        pass
    def updateHeader(self):
        self.headerItm = SimpleProfileHeader(None, self, self.profile,
                                             QRectF(0, 0, self.totalWidth, 120),
                                             QPointF(0, 0),
                                             self.graphicPen)
    def updateProfile(self):
        pass
