from PatternLegendItem import *

class LithologyLegendItem(PatternLegendItem):
    def __init__(self, parent, scene, rect, pen, font, lithology):
        PatternLegendItem.__init__(self, parent, scene, rect, pen, font, lithology)
