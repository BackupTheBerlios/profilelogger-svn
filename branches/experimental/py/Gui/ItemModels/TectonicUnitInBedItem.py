from StandardItem import StandardItem

class TectonicUnitInBedItem(StandardItem):
    def __init__(self, tectonicUnitInBed):
        StandardItem.__init__(self, tectonicUnitInBed)
        self.showData()
