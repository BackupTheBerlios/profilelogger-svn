from StandardItem import StandardItem

class BedItem(StandardItem):
    def __init__(self, bed):
        StandardItem.__init__(self, bed)
        self.showData()
