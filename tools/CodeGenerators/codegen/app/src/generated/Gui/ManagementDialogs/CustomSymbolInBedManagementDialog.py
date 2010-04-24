from InBedManagementDialog import *

from Gui.ItemModels.CustomSymbolInBedItemModel import *
from Gui.ItemViews.CustomSymbolInBedItemView import *

class CustomSymbolInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Custom Symbols'):
        InBedManagementDialog.__init__(self, parent, bed, 'Custom Symbols')
        self.addManagementWidget(CustomSymbolInBedItemView)
        self.addCloseButton()
