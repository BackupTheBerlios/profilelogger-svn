from StandardItem import StandardItem

class CustomSymbolInBedItem(StandardItem):
    def __init__(self, customSymbolInBed):
        StandardItem.__init__(self, customSymbolInBed)
        self.showData()
