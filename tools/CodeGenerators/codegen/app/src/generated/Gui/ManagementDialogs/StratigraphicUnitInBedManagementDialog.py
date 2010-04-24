from InBedManagementDialog import *

from Gui.ItemModels.StratigraphicUnitInBedItemModel import *
from Gui.ItemViews.StratigraphicUnitInBedItemView import *

class StratigraphicUnitInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Stratigraphic Units'):
        InBedManagementDialog.__init__(self, parent, bed, 'Stratigraphic Units')
        self.addManagementWidget(StratigraphicUnitInBedItemView)
        self.addCloseButton()
