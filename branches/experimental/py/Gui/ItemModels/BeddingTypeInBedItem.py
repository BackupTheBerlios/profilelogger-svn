from StandardItem import StandardItem

class BeddingTypeInBedItem(StandardItem):
    def __init__(self, beddingTypeInBed):
        StandardItem.__init__(self, beddingTypeInBed)
        self.showData()
