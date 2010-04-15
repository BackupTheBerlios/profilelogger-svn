from ManagementDialog import *

from Gui.ItemModels.GrainSizeTypeItemModel import *
from Gui.ItemViews.GrainSizeTypeItemView import *

class GrainSizeTypeManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(GrainSizeTypeItemView)
        self.addCloseButton()
