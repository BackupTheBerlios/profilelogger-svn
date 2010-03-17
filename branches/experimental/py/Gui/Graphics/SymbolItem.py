from GraphicsRectItem import GraphicsRectItem

class SymbolItem(GraphicsRectItem):
    def __init__(self, parent, scene, symbol):
        GraphicsRectItem.__init__(self, parent, scene)
        self.symbol = symbol
