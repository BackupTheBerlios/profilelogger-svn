from StandardItem import StandardItem

class LithologicalUnitInBedItem(StandardItem):
    def __init__(self, lithologicalUnitInBed):
        StandardItem.__init__(self, lithologicalUnitInBed)
        self.showData()
