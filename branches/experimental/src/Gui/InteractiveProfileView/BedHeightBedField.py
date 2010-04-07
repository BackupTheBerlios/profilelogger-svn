from BedField import *

from BedHeightItem import *

class BedHeightBedField(BedField):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, bed):
        BedField.__init__(self, parent, scene, rect, pos, font, profileColumn, bed)
        self.bedHeightItm = BedHeightItem(self, self.font, QPointF(0, 0), self.bed)
        self.bedHeightItm.setPos(QPointF((self.rect().width() - self.bedHeightItm.boundingRect().width()) / 2,
                                         (self.rect().height() - self.bedHeightItm.boundingRect().height()) / 2))
