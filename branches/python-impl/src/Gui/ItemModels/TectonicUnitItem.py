from StandardItem import StandardItem

class TectonicUnitItem(StandardItem):
    def __init__(self, tectonicUnit):
        StandardItem.__init__(self, tectonicUnit)
        self.showData()
