from ManagementDialog import *

from Gui.ItemModels.LithologicalUnitTypeItemModel import *
from Gui.ItemViews.LithologicalUnitTypeItemView import *

class LithologicalUnitTypeManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(LithologicalUnitTypeItemView, LithologicalUnitTypeItemModel)
        self.addCloseButton()
