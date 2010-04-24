from InProjectManagementDialog import *

from Gui.ItemModels.TectonicUnitTypeItemModel import *
from Gui.ItemViews.TectonicUnitTypeItemView import *

class TectonicUnitTypeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Tectonic Unit Types'):
        InProjectManagementDialog.__init__(self, parent, project, 'Tectonic Unit Types')
        self.addManagementWidget(TectonicUnitTypeItemView)
        self.addCloseButton()
