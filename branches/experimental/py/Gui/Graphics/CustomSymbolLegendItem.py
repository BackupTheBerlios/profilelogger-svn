from SymbolLegendItem import *

class CustomSymbolLegendItem(SymbolLegendItem):
    def __init__(self, parent, scene, rect, pen, font, customSymbol):
        SymbolLegendItem.__init__(self, parent, scene, rect, pen, font, customSymbol)
