from LegendItemGroup import *

from LithologicalUnitLegendItem import *

class LithologicalUnitLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Lithological Units')), 
                                 profile,
                                 LithologicalUnitLegendItem)
        self.createItems(self.profile.project.lithologicalUnits)
