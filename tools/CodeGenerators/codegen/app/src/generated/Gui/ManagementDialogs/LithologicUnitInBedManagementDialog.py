from InBedManagementDialog import *

from Gui.ItemModels.LithologicUnitInBedItemModel import *
from Gui.ItemViews.LithologicUnitInBedItemView import *

class LithologicUnitInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Lithologic Units'):
        InBedManagementDialog.__init__(self, parent, bed, 'Lithologic Units')
        self.addManagementWidget(LithologicUnitInBedItemView)
        self.addCloseButton()
