from InBedManagementDialog import *

from Gui.ItemModels.GrainSizeInBedItemModel import *
from Gui.ItemViews.GrainSizeInBedItemView import *

class GrainSizeInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Grain Sizes'):
        InBedManagementDialog.__init__(self, parent, bed, 'Grain Sizes')
        self.addManagementWidget(GrainSizeInBedItemView)
        self.addCloseButton()
