from InBedManagementDialog import *

from Gui.ItemModels.SedimentologicUnitInBedItemModel import *
from Gui.ItemViews.SedimentologicUnitInBedItemView import *

class SedimentologicUnitInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Sedimentologic Units'):
        InBedManagementDialog.__init__(self, parent, bed, 'Sedimentologic Units')
        self.addManagementWidget(SedimentologicUnitInBedItemView)
        self.addCloseButton()
