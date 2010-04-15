from DataInProjectManagementDialog import *

from Gui.ItemModels.TectonicUnitItemModel import *
from Gui.ItemViews.TectonicUnitItemView import *

class TectonicUnitManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(TectonicUnitItemView)
        self.addCloseButton()

