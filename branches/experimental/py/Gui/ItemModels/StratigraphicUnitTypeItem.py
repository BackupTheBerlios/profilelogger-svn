from StandardItem import StandardItem

class StratigraphicUnitTypeItem(StandardItem):
    def __init__(self, stratigraphicUnitType):
        StandardItem.__init__(self, stratigraphicUnitType)
        self.showData()
