from PyQt4.QtGui import *
from PyQt4.QtCore import *

from LegendTitle import LegendTitle
from LithologyLegendItem import *
from BeddingTypeLegendItem import *
from ColorLegendItem import *
from TectonicUnitLegendItem import *
from StratigraphicLegendItem import *
from LithologicalUnitLegendItem import *
from SedimentStructureLegendItem import *
from FossilLegendItem import *
from CustomSymbolLegendItem import *
from FaciesLegendItem import *
from OutcropTypeLegendItem import *

class SimpleLegend(QGraphicsRectItem):
    def __init__(self, parent, scene, 
                 profile, 
                 rect, pen,
                 colCount):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.profile = profile
        self.colCount = colCount
        self.currY = 0
        self.setRect(rect)
        self.cellRect = QRectF(0, 0, self.rect().width() / colCount, 1.5*(self.rect().width() / colCount))
        self.setPen(pen)
        self.headerFont = QFont()
        self.headerFont.setPointSize(14)
        self.legendFont = QFont()
        self.legendFont.setPointSize(10)
        self.drawContent()
        self.setPos(QPointF(0, 0 - self.rect().height() - 5))
    def drawContent(self):
        self.drawLithologies()
        self.drawBeddingTypes()
        self.drawColors()
        self.drawFacies()
        self.drawOutcropTypes()
        self.drawTectonicUnits()
        self.drawLithologicalUnits()
        self.drawStratigraphicUnits()
        self.drawSedimentStructures()
        self.drawFossils()
        self.drawCustomSymbols()
        r = self.rect()
        r.setHeight(self.currY)
        self.setRect(r)
    def drawLithologies(self):
        self.lithologiesT = LegendTitle(self, self.scene(), self.headerFont,
                                        QCoreApplication.translate("Graphic Legend Item", "Lithologies"))
        self.lithologiesT.setPos(QPointF(0, self.currY))
        self.currY = self.lithologiesT.pos().y() + self.lithologiesT.boundingRect().height()

        c = 0
        for l in self.profile.project.lithologies:
            itm = LithologyLegendItem(self, self.scene(), 
                                      self.cellRect, self.pen(), 
                                      self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawBeddingTypes(self):
        self.beddingTypesT = LegendTitle(self, self.scene(), self.headerFont,
                                         QCoreApplication.translate("Graphic Legend Item", "Bedding Types"))
        self.beddingTypesT.setPos(QPointF(0, self.currY))
        self.currY = self.beddingTypesT.pos().y() + self.beddingTypesT.boundingRect().height()

        c = 0
        for l in self.profile.project.beddingTypes:
            itm = BeddingTypeLegendItem(self, self.scene(), 
                                        self.cellRect, self.pen(), 
                                        self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawColors(self):
        self.colorsT = LegendTitle(self, self.scene(), self.headerFont,
                                   QCoreApplication.translate("Graphic Legend Item", "Colors"))
        self.colorsT.setPos(QPointF(0, self.currY))
        self.currY = self.colorsT.pos().y() + self.colorsT.boundingRect().height()

        c = 0
        for l in self.profile.project.colors:
            itm = ColorLegendItem(self, self.scene(), 
                                  self.cellRect, self.pen(), 
                                  self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawTectonicUnits(self):
        self.tectonicUnitsT = LegendTitle(self, self.scene(), self.headerFont,
                                   QCoreApplication.translate("Graphic Legend Item", "Tectonic Units"))
        self.tectonicUnitsT.setPos(QPointF(0, self.currY))
        self.currY = self.tectonicUnitsT.pos().y() + self.tectonicUnitsT.boundingRect().height()

        c = 0
        for l in self.profile.project.tectonicUnits:
            itm = TectonicUnitLegendItem(self, self.scene(), 
                                  self.cellRect, self.pen(), 
                                  self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawStratigraphicUnits(self):
        self.stratigraphicUnitsT = LegendTitle(self, self.scene(), self.headerFont,
                                   QCoreApplication.translate("Graphic Legend Item", "Stratigraphic Units"))
        self.stratigraphicUnitsT.setPos(QPointF(0, self.currY))
        self.currY = self.stratigraphicUnitsT.pos().y() + self.stratigraphicUnitsT.boundingRect().height()

        c = 0
        for l in self.profile.project.stratigraphicUnits:
            itm = StratigraphicUnitLegendItem(self, self.scene(), 
                                  self.cellRect, self.pen(), 
                                  self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawLithologicalUnits(self):
        self.lithologicalUnitsT = LegendTitle(self, self.scene(), self.headerFont,
                                   QCoreApplication.translate("Graphic Legend Item", "Lithological Units"))
        self.lithologicalUnitsT.setPos(QPointF(0, self.currY))
        self.currY = self.lithologicalUnitsT.pos().y() + self.lithologicalUnitsT.boundingRect().height()

        c = 0
        for l in self.profile.project.lithologicalUnits:
            itm = LithologicalUnitLegendItem(self, self.scene(), 
                                  self.cellRect, self.pen(), 
                                  self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawSedimentStructures(self):
        self.sedimentStructuresT = LegendTitle(self, self.scene(), self.headerFont,
                                               QCoreApplication.translate("Graphic Legend Item", "Sediment Structures"))
        self.sedimentStructuresT.setPos(QPointF(0, self.currY))
        self.currY = self.sedimentStructuresT.pos().y() + self.sedimentStructuresT.boundingRect().height()

        c = 0
        for l in self.profile.project.sedimentStructures:
            itm = SedimentStructureLegendItem(self, self.scene(), 
                                              self.cellRect, self.pen(), 
                                              self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()

    def drawFossils(self):
        self.fossilsT = LegendTitle(self, self.scene(), self.headerFont,
                                    QCoreApplication.translate("Graphic Legend Item", "Fossils"))
        self.fossilsT.setPos(QPointF(0, self.currY))
        self.currY = self.fossilsT.pos().y() + self.fossilsT.boundingRect().height()

        c = 0
        for l in self.profile.project.fossils:
            itm = FossilLegendItem(self, self.scene(), 
                                   self.cellRect, self.pen(), 
                                   self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawCustomSymbols(self):
        self.customSymbolsT = LegendTitle(self, self.scene(), self.headerFont,
                                    QCoreApplication.translate("Graphic Legend Item", "Custom Symbols"))
        self.customSymbolsT.setPos(QPointF(0, self.currY))
        self.currY = self.customSymbolsT.pos().y() + self.customSymbolsT.boundingRect().height()

        c = 0
        for l in self.profile.project.customSymbols:
            itm = CustomSymbolLegendItem(self, self.scene(), 
                                   self.cellRect, self.pen(), 
                                   self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawFacies(self):
        self.faciesT = LegendTitle(self, self.scene(), self.headerFont,
                                   QCoreApplication.translate("Graphic Legend Item", "Facies"))
        self.faciesT.setPos(QPointF(0, self.currY))
        self.currY = self.faciesT.pos().y() + self.faciesT.boundingRect().height()

        c = 0
        for l in self.profile.project.facies:
            itm = FaciesLegendItem(self, self.scene(), 
                                   self.cellRect, self.pen(), 
                                   self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
    def drawOutcropTypes(self):
        self.outcropTypesT = LegendTitle(self, self.scene(), self.headerFont,
                                   QCoreApplication.translate("Graphic Legend Item", "Outcrop Types"))
        self.outcropTypesT.setPos(QPointF(0, self.currY))
        self.currY = self.outcropTypesT.pos().y() + self.outcropTypesT.boundingRect().height()

        c = 0
        for l in self.profile.project.outcropTypes:
            itm = OutcropTypeLegendItem(self, self.scene(), 
                                  self.cellRect, self.pen(), 
                                  self.legendFont, l)
            itm.setPos(QPointF(c * self.cellRect.width(), self.currY))

            c += 1
            if c == self.colCount:
                c = 0
                self.currY += self.cellRect.height()
        self.currY += self.cellRect.height()
