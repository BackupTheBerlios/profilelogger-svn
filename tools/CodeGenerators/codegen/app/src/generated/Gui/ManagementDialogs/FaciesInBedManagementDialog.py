from InBedManagementDialog import *

from Gui.ItemModels.FaciesInBedItemModel import *
from Gui.ItemViews.FaciesInBedItemView import *

class FaciesInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Facies'):
        InBedManagementDialog.__init__(self, parent, bed, 'Facies')
        self.addManagementWidget(FaciesInBedItemView)
        self.addCloseButton()
