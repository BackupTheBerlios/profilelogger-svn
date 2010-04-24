from InBedManagementDialog import *

from Gui.ItemModels.OutcropTypeInBedItemModel import *
from Gui.ItemViews.OutcropTypeInBedItemView import *

class OutcropTypeInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Outcrop Types'):
        InBedManagementDialog.__init__(self, parent, bed, 'Outcrop Types')
        self.addManagementWidget(OutcropTypeInBedItemView)
        self.addCloseButton()
