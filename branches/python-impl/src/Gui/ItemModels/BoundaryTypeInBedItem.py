from StandardItem import StandardItem

class BoundaryTypeInBedItem(StandardItem):
    def __init__(self, boundaryTypeInBed):
        StandardItem.__init__(self, boundaryTypeInBed)
        self.showData()
