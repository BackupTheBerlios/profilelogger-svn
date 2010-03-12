from StandardItem import StandardItem

class StratigraphicUnitItem(StandardItem):
    def __init__(self, stratigraphicUnit):
        StandardItem.__init__(self, stratigraphicUnit)
        self.showData()
