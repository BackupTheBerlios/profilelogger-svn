from ManagementDialog import *

from Gui.ItemModels.TectonicUnitTypeItemModel import *
from Gui.ItemViews.TectonicUnitTypeItemView import *

class TectonicUnitTypeManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(TectonicUnitTypeItemView, TectonicUnitTypeItemModel)
        self.addCloseButton()
