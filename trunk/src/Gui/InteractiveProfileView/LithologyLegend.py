from LegendItemGroup import *

from LithologyLegendItem import *

class LithologyLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Lithologies')), 
                                 profile,
                                 LithologyLegendItem)
        self.createItems(self.profile.project.lithologies)
