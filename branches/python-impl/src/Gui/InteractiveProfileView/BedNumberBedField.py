from BedField import *

from BedNumberItem import *

class BedNumberBedField(BedField):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, bed):
        BedField.__init__(self, parent, scene, rect, pos, font, profileColumn, bed)
        self.bedNumberItm = BedNumberItem(self, self.font, QPointF(0, 0), self.bed)
        self.bedNumberItm.setPos(QPointF((self.rect().width() - self.bedNumberItm.boundingRect().width()) / 2,
                                         (self.rect().height() - self.bedNumberItm.boundingRect().height()) / 2))
