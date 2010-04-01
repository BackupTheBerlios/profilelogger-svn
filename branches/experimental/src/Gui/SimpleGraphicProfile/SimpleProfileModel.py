from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SimpleProfileHeader import *
from SimpleProfile import *
from SimpleLegend import *

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
from BeddingTypeHeaderItem import *

class SimpleProfileModel(QGraphicsScene):
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.profile = None
        self.columnWidths = dict()
        self.columnSequence = []
        self.totalWidth = 0
        self.graphicPen = QPen(Qt.black)
        self.graphicPen.setStyle(Qt.SolidLine)
        self.graphicPen.setCapStyle(Qt.RoundCap)
        self.graphicPen.setJoinStyle(Qt.RoundJoin)
        self.setupColumnWidths()
        self.setupColumnSequence()
    def setProfile(self, profile):
        self.profile = profile
        self.updateItems()
    def setupColumnWidths(self):
        self.columnWidths[HeightHeaderItem] = 80
        self.columnWidths[BedHeaderItem] = 50
        self.columnWidths[LithologyHeaderItem] = 100
        self.columnWidths[BeddingTypeHeaderItem] = 100
        self.columnWidths[GrainSizeHeaderItem] = 200
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
    def setupColumnSequence(self):
        self.columnSequence.append(HeightHeaderItem)
        self.columnSequence.append(BedHeaderItem)
        self.columnSequence.append(BeddingTypeHeaderItem)
        self.columnSequence.append(LithologyHeaderItem)
        self.columnSequence.append(GrainSizeHeaderItem)
        self.columnSequence.append(ColorHeaderItem)
        self.columnSequence.append(FossilHeaderItem)
        self.columnSequence.append(SedimentStructureHeaderItem)
        self.columnSequence.append(CustomSymbolHeaderItem)
        self.columnSequence.append(TectonicUnitHeaderItem)
        self.columnSequence.append(LithologicalUnitHeaderItem)
        self.columnSequence.append(StratigraphicUnitHeaderItem)
        self.columnSequence.append(FaciesHeaderItem)
        self.columnSequence.append(OutcropTypeHeaderItem)
    def updateItems(self):
        self.clear()
        if self.profile is not None:
            self.updateLegend()
            self.updateHeader()
            self.updateProfile()
    def updateLegend(self):
        self.legendItm = SimpleLegend(None, self, self.profile,
                                      QRectF(0, 0, self.totalWidth, 10),
                                      self.graphicPen,
                                      8)
    def updateHeader(self):
        self.headerItm = SimpleProfileHeader(None, self, self.profile,
                                             QRectF(0, 0, self.totalWidth, 120),
                                             QPointF(0, 0),
                                             self.graphicPen,
                                             self.columnWidths,
                                             self.columnSequence)
    def updateProfile(self):
        self.profileItm = SimpleProfile(None, self, self.profile,
                                        QRectF(0, 0, 
                                               self.totalWidth, self.profileHeight()),
                                        QPointF(0, self.headerItm.rect().height()),
                                        self.graphicPen,
                                        self.columnWidths,
                                        self.columnSequence)
    def profileHeight(self):
        return self.profile.heightInMillimetres() / self.profile.scale
    def scaleLengthToPixel(self, value, unit):
        return self.scaleMillimetresToPixel(value * unit.microMetre/1000)
    def scaleMillimetresToPixel(self, mm):
        return mm / self.profile.scale
