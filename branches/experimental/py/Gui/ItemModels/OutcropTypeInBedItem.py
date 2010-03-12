from StandardItem import StandardItem

class OutcropTypeInBedItem(StandardItem):
    def __init__(self, outcropTypeInBed):
        StandardItem.__init__(self, outcropTypeInBed)
        self.showData()
