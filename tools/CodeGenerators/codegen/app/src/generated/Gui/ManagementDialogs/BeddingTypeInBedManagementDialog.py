from InBedManagementDialog import *

from Gui.ItemModels.BeddingTypeInBedItemModel import *
from Gui.ItemViews.BeddingTypeInBedItemView import *

class BeddingTypeInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Bedding Types'):
        InBedManagementDialog.__init__(self, parent, bed, 'Bedding Types')
        self.addManagementWidget(BeddingTypeInBedItemView)
        self.addCloseButton()
