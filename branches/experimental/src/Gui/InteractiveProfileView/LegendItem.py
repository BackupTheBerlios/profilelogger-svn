from InteractiveRectItem import *

from LithologyLegend import *
from BeddingTypeLegend import *
from ColorLegend import *
from OutcropTypeLegend import *
from FaciesLegend import *
from LithologicalUnitLegend import *
from TectonicUnitLegend import *
from StratigraphicUnitLegend import *

class LegendItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect)
        self.headerFont = headerFont
        self.legendFont = legendFont
        self.profile = profile
        self.maxY = 0
        self.drawLithologies()
        self.drawBeddingTypes()
        self.drawColors()
        self.drawOutcropTypes()
        self.drawFacies()
        self.drawLithologicalUnits()
        self.drawTectonicUnits()
        self.drawStratigraphicUnits()
        self.setRect(QRectF(0, 0, self.rect().width(), self.maxY))
    def drawLithologies(self):
        self.lithologyL = LithologyLegend(self, 
                                          self.scene(),
                                          QRectF(0, 0, self.rect().width(), 0),
                                          QPointF(0, self.maxY),
                                          self.headerFont,
                                          self.legendFont,
                                          self.profile)
        self.maxY += self.lithologyL.rect().height()
    def drawBeddingTypes(self):
        self.beddingTypeL = BeddingTypeLegend(self,
                                              self.scene(),
                                              QRectF(0, 0, self.rect().width(), 0),
                                              QPointF(0, self.maxY),
                                              self.headerFont,
                                              self.legendFont,
                                              self.profile)
        self.maxY += self.beddingTypeL.rect().height()
    def drawColors(self):
        self.colorL = ColorLegend(self, 
                                  self.scene(),
                                  QRectF(0, 0, self.rect().width(), 0),
                                  QPointF(0, self.maxY),
                                  self.headerFont,
                                  self.legendFont,
                                  self.profile)
        self.maxY += self.colorL.rect().height()
    def drawOutcropTypes(self):
        self.outcropTypeL = OutcropTypeLegend(self, 
                                              self.scene(),
                                              QRectF(0, 0, self.rect().width(), 0),
                                              QPointF(0, self.maxY),
                                              self.headerFont,
                                              self.legendFont,
                                              self.profile)
        self.maxY += self.outcropTypeL.rect().height()
    def drawFacies(self):
        self.faciesL = FaciesLegend(self, 
                                    self.scene(),
                                    QRectF(0, 0, self.rect().width(), 0),
                                    QPointF(0, self.maxY),
                                    self.headerFont,
                                    self.legendFont,
                                    self.profile)
        self.maxY += self.faciesL.rect().height()
    def drawLithologicalUnits(self):
        self.lithologicalUnitL = LithologicalUnitLegend(self, 
                                                        self.scene(),
                                                        QRectF(0, 0, self.rect().width(), 0),
                                                        QPointF(0, self.maxY),
                                                        self.headerFont,
                                                        self.legendFont,
                                                        self.profile)
        self.maxY += self.lithologicalUnitL.rect().height()
    def drawTectonicUnits(self):
        self.tectonicUnitL = TectonicUnitLegend(self, 
                                                self.scene(),
                                                QRectF(0, 0, self.rect().width(), 0),
                                                QPointF(0, self.maxY),
                                                self.headerFont,
                                                self.legendFont,
                                                self.profile)
        self.maxY += self.tectonicUnitL.rect().height()
    def drawStratigraphicUnits(self):
        self.stratigraphicUnitL = StratigraphicUnitLegend(self, 
                                                          self.scene(),
                                                          QRectF(0, 0, self.rect().width(), 0),
                                                          QPointF(0, self.maxY),
                                                          self.headerFont,
                                                          self.legendFont,
                                                          self.profile)
        self.maxY += self.stratigraphicUnitL.rect().height()
