from StandardItem import StandardItem

class ColorInBedItem(StandardItem):
    def __init__(self, colorInBed):
        StandardItem.__init__(self, colorInBed)
        self.showData()
