from ManagementDialog import *

from Gui.ItemModels.GrainSizeItemModel import *
from Gui.ItemViews.GrainSizeItemView import *

class GrainSizeManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(GrainSizeItemView)
        self.addCloseButton()
