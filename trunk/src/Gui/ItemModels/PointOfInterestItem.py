from StandardItem import StandardItem

class PointOfInterestItem(StandardItem):
    def __init__(self, pointOfInterest):
        StandardItem.__init__(self, pointOfInterest)
        self.showData()
