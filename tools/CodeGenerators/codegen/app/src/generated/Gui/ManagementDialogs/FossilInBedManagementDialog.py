from InBedManagementDialog import *

from Gui.ItemModels.FossilInBedItemModel import *
from Gui.ItemViews.FossilInBedItemView import *

class FossilInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Fossils'):
        InBedManagementDialog.__init__(self, parent, bed, 'Fossils')
        self.addManagementWidget(FossilInBedItemView)
        self.addCloseButton()
