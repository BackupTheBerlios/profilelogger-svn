from StandardItem import StandardItem

class StratigraphicUnitInBedItem(StandardItem):
    def __init__(self, stratigraphicUnitInBed):
        StandardItem.__init__(self, stratigraphicUnitInBed)
        self.showData()
