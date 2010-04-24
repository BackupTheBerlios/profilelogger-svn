from InBedManagementDialog import *

from Gui.ItemModels.BoundaryTypeInBedItemModel import *
from Gui.ItemViews.BoundaryTypeInBedItemView import *

class BoundaryTypeInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Boundary Types'):
        InBedManagementDialog.__init__(self, parent, bed, 'Boundary Types')
        self.addManagementWidget(BoundaryTypeInBedItemView)
        self.addCloseButton()
