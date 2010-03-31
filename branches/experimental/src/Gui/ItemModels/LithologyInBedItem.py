from StandardItem import StandardItem

class LithologyInBedItem(StandardItem):
    def __init__(self, lithologyInBed):
        StandardItem.__init__(self, lithologyInBed)
        self.showData()
