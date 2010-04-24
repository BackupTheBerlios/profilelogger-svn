from InBedManagementDialog import *

from Gui.ItemModels.ColorInBedItemModel import *
from Gui.ItemViews.ColorInBedItemView import *

class ColorInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Colors'):
        InBedManagementDialog.__init__(self, parent, bed, 'Colors')
        self.addManagementWidget(ColorInBedItemView)
        self.addCloseButton()
