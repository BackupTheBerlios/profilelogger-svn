from InProjectManagementDialog import *

from Gui.ItemModels.GrainSizeItemModel import *
from Gui.ItemViews.GrainSizeItemView import *

class GrainSizeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Grain Sizes'):
        InProjectManagementDialog.__init__(self, parent, project, 'Grain Sizes')
        self.addManagementWidget(GrainSizeItemView)
        self.addCloseButton()
