from InteractiveRectItem import *

from BedHeightHeader import *
from BedNumberHeader import *
from BeddingTypeHeader import *
from LithologyHeader import *
from FossilHeader import *
from SedimentStructureHeader import *
from CustomSymbolHeader import *
from LithologicalUnitHeader import *
from TectonicUnitHeader import *
from StratigraphicUnitHeader import *
from FaciesHeader import *
from ColorHeader import *
from GrainSizeHeader import *

class ProfileHeaderItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.headerFont = headerFont
        self.legendFont = legendFont
        self.profile = profile
        self.maxX = 0
        self.setRect(QRectF(0, 0, self.rect().width(), self.rect().width() / 6))
        self.drawItems()
    def drawItems(self):
        for c in self.profile.columns:
            self.drawColumnHeader(c)
    def drawHeader(self, col, headerClass):
        headerClass(self,
                    self.scene(),
                    QRectF(0, 0, 
                           col.width, self.rect().height()),
                    QPointF(self.maxX, 0),
                    self.headerFont,
                    col,
                    -90)
    def drawColumnHeader(self, col):
        className = col.profileColumn.headerClassName
        if className == 'BedHeightHeader':
            self.drawHeader(col, BedHeightHeader)
        if className == 'BedNumberHeader':
            self.drawHeader(col, BedNumberHeader)
        if className == 'BeddingTypeHeader':
            self.drawHeader(col, BeddingTypeHeader)
        if className == 'LithologyHeader':
            self.drawHeader(col, LithologyHeader)
        if className == 'FossilHeader':
            self.drawHeader(col, FossilHeader)
        if className == 'SedimentStructureHeader':
            self.drawHeader(col, SedimentStructureHeader)
        if className == 'CustomSymbolHeader':
            self.drawHeader(col, CustomSymbolHeader)
        if className == 'LithologicalUnitHeader':
            self.drawHeader(col, LithologicalUnitHeader)
        if className == 'TectonicUnitHeader':
            self.drawHeader(col, TectonicUnitHeader)
        if className == 'StratigraphicUnitHeader':
            self.drawHeader(col, StratigraphicUnitHeader)
        if className == 'FaciesHeader':
            self.drawHeader(col, FaciesHeader)
        if className == 'ColorHeader':
            self.drawHeader(col, ColorHeader)
        if className == 'GrainSizeHeader':
            self.drawHeader(col, GrainSizeHeader)
        self.maxX += col.width
