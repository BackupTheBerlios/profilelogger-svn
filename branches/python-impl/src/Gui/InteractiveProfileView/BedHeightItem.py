from TextItem import *

class BedHeightItem(TextItem):
    def __init__(self, parent, font, pos, bed):
        TextItem.__init__(self, parent, font, pos)
        self.bed = bed
        self.setText(bed.getFormattedHeight())
