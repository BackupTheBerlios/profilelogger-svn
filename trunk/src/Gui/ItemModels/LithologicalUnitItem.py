from StandardItem import StandardItem

class LithologicalUnitItem(StandardItem):
    def __init__(self, lithologicalUnit):
        StandardItem.__init__(self, lithologicalUnit)
        self.showData()
