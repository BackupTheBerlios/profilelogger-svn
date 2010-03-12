from StandardItem import StandardItem

class LithologicalUnitTypeItem(StandardItem):
    def __init__(self, lithologicalUnitType):
        StandardItem.__init__(self, lithologicalUnitType)
        self.showData()
