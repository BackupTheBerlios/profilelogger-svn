from TextItem import *

class BedNumberItem(TextItem):
    def __init__(self, parent, font, pos, bed):
        TextItem.__init__(self, parent, font, pos)
        self.bed = bed
        self.setText(QString.number(bed.number))
