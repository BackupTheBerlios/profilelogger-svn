from StandardItem import StandardItem

class FaciesInBedItem(StandardItem):
    def __init__(self, faciesInBed):
        StandardItem.__init__(self, faciesInBed)
        self.showData()
