from PatternLegendItem import *

class ColorLegendItem(PatternLegendItem):
    def __init__(self, parent, scene, rect, pen, font, color):
        PatternLegendItem.__init__(self, parent, scene, rect, pen, font, color)
