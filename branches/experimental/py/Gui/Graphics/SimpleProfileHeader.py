from PyQt4.QtGui import *
from PyQt4.QtCore import *

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

class SimpleProfileHeader(QGraphicsRectItem):
    def __init__(self, parent, scene, 
                 profile, 
                 rect, pos, pen, 
                 columnWidths, columnSequence):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.profile = profile
        self.columnWidths = columnWidths
        self.columnSequence = columnSequence
        self.headerItems = dict()
        self.setRect(rect)
        self.setPos(pos)
        self.setPen(pen)
        self.setupRects()
        self.drawHeaderItems()
    def drawHeaderItems(self):
        self.headerItems = dict()
        x = 0
        for headerClass in self.columnSequence:
            self.headerItems[headerClass] = headerClass(self, self.scene(), 
                                                        QRectF(0, 0, 
                                                               self.columnWidths[headerClass], self.rect().height()),
                                                        self.pen())
            self.headerItems[headerClass].setPos(QPointF(x, 0))
            x += self.columnWidths[headerClass]
