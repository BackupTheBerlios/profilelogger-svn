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
    def __init__(self, parent, scene, profile, rect, pos, pen, columnWidths):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.profile = profile
        self.columnWidths = columnWidths
        self.setRect(rect)
        self.setPos(pos)
        self.setPen(pen)
        self.setupRects()
        self.drawHeaderItems()
    def setupRects(self):
        self.heightRect = QRectF(0, 0, self.columnWidths[HeightHeaderItem], 
                                 self.rect().height())
        self.bedRect = QRectF(0, 0, self.columnWidths[BedHeaderItem], 
                              self.rect().height())
        self.lithologyRect = QRectF(0, 0, self.columnWidths[LithologyHeaderItem], 
                                    self.rect().height())
        self.grainSizeRect = QRectF(0, 0, self.columnWidths[GrainSizeHeaderItem], 
                                    self.rect().height())
        self.colorRect = QRectF(0, 0, self.columnWidths[ColorHeaderItem], 
                                self.rect().height())
        self.fossilRect = QRectF(0, 0, self.columnWidths[FossilHeaderItem], 
                                 self.rect().height())
        self.sedimentStructureRect = QRectF(0, 0, self.columnWidths[SedimentStructureHeaderItem], 
                                            self.rect().height())
        self.customSymbolRect = QRectF(0, 0, self.columnWidths[CustomSymbolHeaderItem], 
                                       self.rect().height())
        self.tectonicUnitRect = QRectF(0, 0, self.columnWidths[TectonicUnitHeaderItem], 
                                       self.rect().height())
        self.stratigraphicUnitRect = QRectF(0, 0, self.columnWidths[StratigraphicUnitHeaderItem], 
                                            self.rect().height())
        self.lithologicalUnitRect = QRectF(0, 0, self.columnWidths[LithologicalUnitHeaderItem], 
                                           self.rect().height())
        self.faciesRect = QRectF(0, 0, self.columnWidths[FaciesHeaderItem], 
                                 self.rect().height())
        self.outcropTypeRect = QRectF(0, 0, self.columnWidths[OutcropTypeHeaderItem], 
                                      self.rect().height())
    def drawHeaderItems(self):
        x = 0
        self.heightItm = HeightHeaderItem(self, self.scene(), self.heightRect, self.pen())
        self.heightItm.setPos(QPointF(x, 0))
        x += self.heightRect.width()

        self.bedItm = BedHeaderItem(self, self.scene(), self.bedRect, self.pen())
        self.bedItm.setPos(QPointF(x, 0))
        x += self.bedRect.width()

        self.lithologyItm = LithologyHeaderItem(self, self.scene(), self.lithologyRect, self.pen())
        self.lithologyItm.setPos(QPointF(x, 0))
        x += self.lithologyRect.width()

        self.grainSizeItm = GrainSizeHeaderItem(self, self.scene(), self.grainSizeRect, self.pen())
        self.grainSizeItm.setPos(QPointF(x, 0))
        x += self.grainSizeRect.width()

        self.fossilItm = FossilHeaderItem(self, self.scene(), self.fossilRect, self.pen())
        self.fossilItm.setPos(QPointF(x, 0))
        x += self.fossilRect.width()

        self.sedimentStructureItm = SedimentStructureHeaderItem(self, self.scene(), self.sedimentStructureRect, self.pen())
        self.sedimentStructureItm.setPos(QPointF(x, 0))
        x += self.sedimentStructureRect.width()

        self.customSymbolItm = CustomSymbolHeaderItem(self, self.scene(), self.customSymbolRect, self.pen())
        self.customSymbolItm.setPos(QPointF(x, 0))
        x += self.customSymbolRect.width()


        self.colorItm = ColorHeaderItem(self, self.scene(), self.colorRect, self.pen())
        self.colorItm.setPos(QPointF(x, 0))
        x += self.colorRect.width()

        self.tectonicUnitItm = TectonicUnitHeaderItem(self, self.scene(), self.tectonicUnitRect, self.pen())
        self.tectonicUnitItm.setPos(QPointF(x, 0))
        x += self.tectonicUnitRect.width()

        self.stratigraphicUnitItm = StratigraphicUnitHeaderItem(self, self.scene(), self.stratigraphicUnitRect, self.pen())
        self.stratigraphicUnitItm.setPos(QPointF(x, 0))
        x += self.stratigraphicUnitRect.width()

        self.lithologicalUnitItm = LithologicalUnitHeaderItem(self, self.scene(), self.lithologicalUnitRect, self.pen())
        self.lithologicalUnitItm.setPos(QPointF(x, 0))
        x += self.lithologicalUnitRect.width()

        self.faciesItm = FaciesHeaderItem(self, self.scene(), self.faciesRect, self.pen())
        self.faciesItm.setPos(QPointF(x, 0))
        x += self.faciesRect.width()

        self.outcropTypeItm = OutcropTypeHeaderItem(self, self.scene(), self.outcropTypeRect, self.pen())
        self.outcropTypeItm.setPos(QPointF(x, 0))
        x += self.outcropTypeRect.width()
