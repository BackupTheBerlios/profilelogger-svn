from LegendItemGroup import *

from CustomSymbolLegendItem import *

class CustomSymbolLegend(LegendItemGroup):
    def __init__(self, parent, scene, rect, pos, headerFont, legendFont, profile):
        LegendItemGroup.__init__(self, 
                                 parent, 
                                 scene, 
                                 rect, 
                                 pos, 
                                 headerFont, 
                                 legendFont,
                                 unicode(QCoreApplication.translate('legend header', 'Custom Symbols')), 
                                 profile,
                                 CustomSymbolLegendItem)
        self.createItems(self.profile.project.customSymbols)
