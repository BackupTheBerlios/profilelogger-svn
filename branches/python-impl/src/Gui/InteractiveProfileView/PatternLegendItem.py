from LegendDataItem import *

from Gui.SimpleGraphicProfile.BrushFactory import *

class PatternLegendItem(LegendDataItem):
    def __init__(self, parent, scene, rect, pos, font, data):
        LegendDataItem.__init__(self, parent, scene, rect, pos, font, data)
        self.createDisplay()
        self.createIdDisplay()
        self.createNameDisplay()
        self.fillDisplay()
    def fillDisplay(self):
        if not self.hasData():
            return
        f = BrushFactory(self.scene())
        if self.data.hasSvgItem():
            brush = f.fromSvgItem(self.data.svgItem)
            self.displayItm.setBrush(brush)
