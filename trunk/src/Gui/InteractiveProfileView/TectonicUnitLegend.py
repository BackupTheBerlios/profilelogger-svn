from LegendItemGroup import *

from TectonicUnitLegendItem import *

class TectonicUnitLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Tectonic Units')), 
                                 profile,
                                 TectonicUnitLegendItem)
        self.createItems(self.profile.project.tectonicUnits)
