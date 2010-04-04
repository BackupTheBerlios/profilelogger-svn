from LegendItemGroup import *

from FaciesLegendItem import *

class FaciesLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Facies')), 
                                 profile,
                                 FaciesLegendItem)
        self.createItems(self.profile.project.facies)
