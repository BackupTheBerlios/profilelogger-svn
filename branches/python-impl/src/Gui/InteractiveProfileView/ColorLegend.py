from LegendItemGroup import *

from ColorLegendItem import *

class ColorLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Colors')), 
                                 profile,
                                 ColorLegendItem)
        self.createItems(self.profile.project.colors)
