from LegendItemGroup import *

from OutcropTypeLegendItem import *

class OutcropTypeLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Outcrop Types')), 
                                 profile,
                                 OutcropTypeLegendItem)
        self.createItems(self.profile.project.outcropTypes)
