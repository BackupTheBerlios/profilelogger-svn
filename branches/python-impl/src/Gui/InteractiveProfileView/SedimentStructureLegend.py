from LegendItemGroup import *

from SedimentStructureLegendItem import *

class SedimentStructureLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Sediment Structures')), 
                                 profile,
                                 SedimentStructureLegendItem)
        self.createItems(self.profile.project.sedimentStructures)
