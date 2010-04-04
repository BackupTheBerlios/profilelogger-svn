from LegendItemGroup import *

from BeddingTypeLegendItem import *

class BeddingTypeLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Bedding Types')), 
                                 profile,
                                 BeddingTypeLegendItem)
        self.createItems(self.profile.project.beddingTypes)
