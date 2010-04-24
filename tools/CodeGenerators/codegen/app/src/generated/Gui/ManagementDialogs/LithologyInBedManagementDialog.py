from InBedManagementDialog import *

from Gui.ItemModels.LithologyInBedItemModel import *
from Gui.ItemViews.LithologyInBedItemView import *

class LithologyInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Lithologies'):
        InBedManagementDialog.__init__(self, parent, bed, 'Lithologies')
        self.addManagementWidget(LithologyInBedItemView)
        self.addCloseButton()
