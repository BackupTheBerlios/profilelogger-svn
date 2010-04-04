from SymbolLegendItem import *

class CustomSymbolLegendItem(SymbolLegendItem):
    def __init__(self, parent, scene, rect, pos, font, customSymbol):
        SymbolLegendItem.__init__(self, parent, scene, rect, pos, font, customSymbol)
