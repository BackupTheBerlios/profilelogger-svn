from StandardItem import StandardItem

class CustomSymbolItem(StandardItem):
    def __init__(self, customSymbol):
        StandardItem.__init__(self, customSymbol)
        self.showData()
