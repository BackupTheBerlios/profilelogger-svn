from InBedManagementDialog import *

from Gui.ItemModels.SedimentStructureInBedItemModel import *
from Gui.ItemViews.SedimentStructureInBedItemView import *

class SedimentStructureInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Sediment Structures'):
        InBedManagementDialog.__init__(self, parent, bed, 'Sediment Structures')
        self.addManagementWidget(SedimentStructureInBedItemView)
        self.addCloseButton()
