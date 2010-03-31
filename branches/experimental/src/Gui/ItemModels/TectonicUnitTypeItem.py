from StandardItem import StandardItem

class TectonicUnitTypeItem(StandardItem):
    def __init__(self, tectonicUnitType):
        StandardItem.__init__(self, tectonicUnitType)
        self.showData()
