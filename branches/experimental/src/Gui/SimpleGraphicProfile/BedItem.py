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
from BeddingTypeHeaderItem import *

from BedNumberText import *
from LithologyItem import *
from GrainSizeItem import *
from ColorItem import *
from FossilItem import *
from SedimentStructureItem import *
from CustomSymbolItem import *
from TectonicUnitItem import *
from LithologicalUnitItem import *
from StratigraphicUnitItem import *
from FaciesItem import *
from OutcropTypeItem import *
from BeddingTypeItem import *

from SymbolFactory import *

class BedItem(QGraphicsRectItem):
    def __init__(self, parent, scene, 
                 bed, 
                 rect, pos, pen, 
                 columnWidths, columnSequence):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.bed = bed
        self.p = QPen(Qt.NoPen)
        self.p.setStyle(Qt.DotLine)
        self.columnWidths = columnWidths
        self.columnSequence = columnSequence
        self.headerItems = dict()
        self.setRect(rect)
        self.setPos(pos)
        self.setPen(QPen(Qt.NoPen))
        self.showFields()
    def showFields(self):
        x = 0
        for headerClass in self.columnSequence:
            if headerClass == HeightHeaderItem:
                self.drawHeight(self.columnWidths[headerClass], x)
            if headerClass == BedHeaderItem:
                self.drawBedNumber(self.columnWidths[headerClass], x)
            if headerClass == LithologyHeaderItem:
                self.drawLithology(self.columnWidths[headerClass], x)
            if headerClass == GrainSizeHeaderItem:
                self.drawGrainSize(self.columnWidths[headerClass], x)
            if headerClass == ColorHeaderItem:
                self.drawColor(self.columnWidths[headerClass], x)
            if headerClass == FossilHeaderItem:
                self.drawFossils(self.columnWidths[headerClass], x)
            if headerClass == SedimentStructureHeaderItem:
                self.drawSedimentStructures(self.columnWidths[headerClass], x)
            if headerClass == CustomSymbolHeaderItem:
                self.drawCustomSymbols(self.columnWidths[headerClass], x)
            if headerClass == TectonicUnitHeaderItem:
                self.drawTectonicUnit(self.columnWidths[headerClass], x)
            if headerClass == LithologicalUnitHeaderItem:
                self.drawLithologicalUnit(self.columnWidths[headerClass], x)
            if headerClass == StratigraphicUnitHeaderItem:
                self.drawStratigraphicUnit(self.columnWidths[headerClass], x)
            if headerClass == FaciesHeaderItem:
                self.drawFacies(self.columnWidths[headerClass], x)
            if headerClass == OutcropTypeHeaderItem:
                self.drawOutcropType(self.columnWidths[headerClass], x)
            if headerClass == BeddingTypeHeaderItem:
                self.drawBeddingType(self.columnWidths[headerClass], x)
            self.drawBoundaryTypes()
            x += self.columnWidths[headerClass]
    def drawVerticalSeparator(self, x, pen = None):
        l = QGraphicsLineItem(self)
#        self.scene().addItem(l)
        l.setLine(QLineF(0, 0, 0, self.rect().height()))
        l.setPos(x, 0)
        if pen is None:
            l.setPen(self.p)
        else:
            l.setPen(pen)
    def drawHeight(self, w, y):
        pass
    def drawBedNumber(self, w, x):
        self.drawVerticalSeparator(x)
        self.bedNumberItm = BedNumberText(self, self.scene(), QFont(), self.bed, 0)
        self.bedNumberItm.adjustSize()
        self.bedNumberItm.setPos(QPointF(x, (self.rect().height() - self.bedNumberItm.boundingRect().height())/2))
    def drawLithology(self, w, x):
        self.lithologyItm = LithologyItem(self, self.scene(),
                                          QRectF(0, 0, w, self.rect().height()),
                                          self.p,
                                          self.bed)
        self.lithologyItm.setPos(QPointF(x, 0))
    def drawGrainSize(self, w, x):
        if len(self.bed.grainSizes) < 1:
            return
        self.grainSizeItm = GrainSizeItem(self, self.scene(),
                                          QRectF(0, 0, w, self.rect().height()),
                                          self.p,
                                          self.bed)
        self.grainSizeItm.setPos(x, 0)
    def drawColor(self, w, x):
        self.colorItm = ColorItem(self, self.scene(),
                                  QRectF(0, 0, w, self.rect().height()),
                                  self.p,
                                  self.bed)
        self.colorItm.setPos(QPointF(x, 0))
    def drawBeddingType(self, w, x):
        self.beddingTypeItm = BeddingTypeItem(self, self.scene(),
                                              QRectF(0, 0, w, self.rect().height()),
                                              self.p,
                                              self.bed)
        self.beddingTypeItm.setPos(QPointF(x, 0))
    def drawFossils(self, w, x):
        self.fossilItm = FossilItem(self, self.scene(),
                                    QRectF(0, 0, w, self.rect().height()),
                                    self.p,
                                    self.bed)
        self.fossilItm.setPos(QPointF(x, 0))
    def drawSedimentStructures(self, w, x):
        self.sedimentStructureItm = SedimentStructureItem(self, self.scene(),
                                                          QRectF(0, 0, w, self.rect().height()),
                                                          self.p,
                                                          self.bed)
        self.sedimentStructureItm.setPos(QPointF(x, 0))
    def drawCustomSymbols(self, w, x):
        self.customSymbolItm = CustomSymbolItem(self, self.scene(),
                                                QRectF(0, 0, w, self.rect().height()),
                                                self.p,
                                                self.bed)
        self.customSymbolItm.setPos(QPointF(x, 0))
    def drawTectonicUnit(self, w, x):
        self.tectonicUnitItm = TectonicUnitItem(self, self.scene(),
                                                QRectF(0, 0, w, self.rect().height()),
                                                self.p,
                                                self.bed)
        self.tectonicUnitItm.setPos(QPointF(x, 0))
    def drawLithologicalUnit(self, w, x):
        self.lithologicalUnitItm = LithologicalUnitItem(self, self.scene(),
                                                        QRectF(0, 0, w, self.rect().height()),
                                                        self.p,
                                                        self.bed)
        self.lithologicalUnitItm.setPos(QPointF(x, 0))
    def drawStratigraphicUnit(self, w, x):
        self.stratigraphicUnitItm = StratigraphicUnitItem(self, self.scene(),
                                                        QRectF(0, 0, w, self.rect().height()),
                                                        self.p,
                                                        self.bed)
        self.stratigraphicUnitItm.setPos(QPointF(x, 0))
    def drawFacies(self, w, x):
        self.faciesItm = FaciesItem(self, self.scene(),
                                    QRectF(0, 0, w, self.rect().height()),
                                    self.p,
                                    self.bed)
        self.faciesItm.setPos(QPointF(x, 0))
    def drawOutcropType(self, w, x):
        self.outcropTypeItm = OutcropTypeItem(self, self.scene(),
                                              QRectF(0, 0, w, self.rect().height()),
                                              self.p,
                                              self.bed)
        self.outcropTypeItm.setPos(QPointF(x, 0))

    def drawBoundaryTypes(self):
        f = SymbolFactory()
        for bt in self.bed.boundaryTypes:
            if bt.boundaryType.hasSvgItem():
                pm = f.pixmapFromSvgItem(bt.boundaryType.svgItem, self.rect().width(), Qt.IgnoreAspectRatio)
                itm = QGraphicsPixmapItem(self, self.scene())
                itm.setPixmap(pm)
                itm.setPos(0, self.rect().height() - bt.begin * self.rect().height() / 100)
