from InProfileManagementDialog import *

from Gui.ItemModels.BedItemModel import *
from Gui.ItemViews.BedItemView import *

class BedManagementDialog(InProfileManagementDialog):
    def __init__(self, parent, profile, 'Beds'):
        InProfileManagementDialog.__init__(self, parent, profile, 'Beds')
        self.addManagementWidget(BedItemView)
        self.addCloseButton()
