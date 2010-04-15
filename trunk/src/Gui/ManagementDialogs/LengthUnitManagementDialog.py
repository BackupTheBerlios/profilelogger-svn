from ManagementDialog import *

from Gui.ItemModels.LengthUnitItemModel import *
from Gui.ItemViews.LengthUnitItemView import *

class LengthUnitManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(LengthUnitItemView)
        self.addCloseButton()
