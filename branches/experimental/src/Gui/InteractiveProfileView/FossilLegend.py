from LegendItemGroup import *

from FossilLegendItem import *

class FossilLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Fossils')), 
                                 profile,
                                 FossilLegendItem)
        self.createItems(self.profile.project.fossils)
