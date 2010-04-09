from StandardItem import StandardItem

class FossilInBedItem(StandardItem):
    def __init__(self, fossilInBed):
        StandardItem.__init__(self, fossilInBed)
        self.showData()
