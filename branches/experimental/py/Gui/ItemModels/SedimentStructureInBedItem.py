from StandardItem import StandardItem

class SedimentStructureInBedItem(StandardItem):
    def __init__(self, sedimentStructureInBed):
        StandardItem.__init__(self, sedimentStructureInBed)
        self.showData()
