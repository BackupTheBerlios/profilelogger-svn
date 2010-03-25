from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SimpleProfileHeader import *

from HeightHeaderItem import *
from BedHeaderItem import *
from LithologyHeaderItem import *
from GrainSizeHeaderItem import *
from ColorHeaderItem import *
from FossilHeaderItem import *
from SedimentStructureHeaderItem import *
from CustomSymbolHeaderItem import *
from TectonicUnitHeaderItem import *
from StratigraphicUnitHeaderItem import *
from LithologicalUnitHeaderItem import *
from FaciesHeaderItem import *
from OutcropTypeHeaderItem import *

class SimpleProfileModel(QGraphicsScene):
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.profile = None
        self.columnWidths = dict()
        self.totalWidth = 0
        self.graphicPen = QPen(Qt.black)
        self.graphicPen.setStyle(Qt.SolidLine)
        self.graphicPen.setCapStyle(Qt.RoundCap)
        self.graphicPen.setJoinStyle(Qt.RoundJoin)
        self.setupColumnWidths()
    def setProfile(self, profile):
        self.profile = profile
        self.updateItems()
    def setupColumnWidths(self):
        self.columnWidths[HeightHeaderItem] = 50
        self.columnWidths[BedHeaderItem] = 50
        self.columnWidths[LithologyHeaderItem] = 100
        self.columnWidths[GrainSizeHeaderItem] = 300
        self.columnWidths[ColorHeaderItem] = 25
        self.columnWidths[FossilHeaderItem] = 50
        self.columnWidths[SedimentStructureHeaderItem] = 50
        self.columnWidths[CustomSymbolHeaderItem] = 50
        self.columnWidths[TectonicUnitHeaderItem] = 25
        self.columnWidths[StratigraphicUnitHeaderItem] = 25
        self.columnWidths[LithologicalUnitHeaderItem] = 25
        self.columnWidths[FaciesHeaderItem] = 25
        self.columnWidths[OutcropTypeHeaderItem] = 25
        self.totalWidth = 0
        for k,v in self.columnWidths.iteritems():
            self.totalWidth += v
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
                                             self.graphicPen,
                                             self.columnWidths)
    def updateProfile(self):
        pass
