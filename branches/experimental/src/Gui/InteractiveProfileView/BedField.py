from RectItem import *

from TextItem import *

class BedField(RectItem):
    def __init__(self, parent, scene, rect, pos, font, profileColumn, bed):
        RectItem.__init__(self, parent, scene, rect, pos)
        self.font = font
        self.profileColumn = profileColumn
        self.bed = bed
        self.setPen(QPen(Qt.black))
