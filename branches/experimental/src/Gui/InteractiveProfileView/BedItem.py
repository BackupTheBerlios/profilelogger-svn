from InteractiveRectItem import *

from BedNumberBedField import *
from BedHeightBedField import *
from BeddingTypeBedField import *
from LithologyBedField import *
from LithologicalUnitBedField import *
from TectonicUnitBedField import *
from StratigraphicUnitBedField import *
from FaciesBedField import *
from ColorBedField import *
from FossilBedField import *
from CustomSymbolBedField import *
from SedimentStructureBedField import *
from GrainSizeBedField import *

class BedItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, legendFont, bed):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.legendFont = legendFont
        self.bed = bed
        self.maxX = 0
        self.setRect(QRectF(0, 0, self.rect().width(), 500))
        self.drawFields()
    def drawFields(self):
        for c in self.bed.profile.columns:
            self.drawColumnContent(c)
            self.maxX += c.width
    def drawColumnContent(self, col):
        className = col.profileColumn.bedPartClassName
        if className == 'BedNumberBedField':
            self.drawField(col, BedNumberBedField)
        if className == 'BedHeightBedField':
            self.drawField(col, BedHeightBedField)
        if className == 'BeddingTypeBedField':
            self.drawField(col, BeddingTypeBedField)
        if className == 'LithologyBedField':
            self.drawField(col, LithologyBedField)
        if className == 'LithologicalUnitBedField':
            self.drawField(col, LithologicalUnitBedField)
        if className == 'TectonicUnitBedField':
            self.drawField(col, TectonicUnitBedField)
        if className == 'StratigraphicUnitBedField':
            self.drawField(col, StratigraphicUnitBedField)
        if className == 'FaciesBedField':
            self.drawField(col, FaciesBedField)
        if className == 'ColorBedField':
            self.drawField(col, ColorBedField)
        if className == 'FossilBedField':
            self.drawField(col, FossilBedField)
        if className == 'CustomSymbolBedField':
            self.drawField(col, CustomSymbolBedField)
        if className == 'SedimentStructureBedField':
            self.drawField(col, SedimentStructureBedField)
        if className == 'GrainSizeBedField':
            self.drawField(col, GrainSizeBedField)

    def drawField(self, col, fieldClass):
        fieldClass(self,
                   self.scene(),
                   QRectF(0, 0, 
                          col.width, self.rect().height()),
                   QPointF(self.maxX, 0),
                   self.legendFont,
                   col,
                   self.bed)
