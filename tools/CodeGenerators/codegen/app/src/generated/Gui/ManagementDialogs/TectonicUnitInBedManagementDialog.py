from InBedManagementDialog import *

from Gui.ItemModels.TectonicUnitInBedItemModel import *
from Gui.ItemViews.TectonicUnitInBedItemView import *

class TectonicUnitInBedManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, 'Tectonic Units'):
        InBedManagementDialog.__init__(self, parent, bed, 'Tectonic Units')
        self.addManagementWidget(TectonicUnitInBedItemView)
        self.addCloseButton()
