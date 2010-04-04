from LegendItemGroup import *

from StratigraphicUnitLegendItem import *

class StratigraphicUnitLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Stratigraphic Units')), 
                                 profile,
                                 StratigraphicUnitLegendItem)
        self.createItems(self.profile.project.stratigraphicUnits)
