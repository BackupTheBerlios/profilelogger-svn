from StandardItem import StandardItem

class BoundaryTypeItem(StandardItem):
    def __init__(self, boundaryType):
        StandardItem.__init__(self, boundaryType)
        self.showData()
