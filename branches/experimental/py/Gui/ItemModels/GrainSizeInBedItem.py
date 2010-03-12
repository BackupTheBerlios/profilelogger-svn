from StandardItem import StandardItem

class GrainSizeInBedItem(StandardItem):
    def __init__(self, grainSizeInBed):
        StandardItem.__init__(self, grainSizeInBed)
        self.showData()
