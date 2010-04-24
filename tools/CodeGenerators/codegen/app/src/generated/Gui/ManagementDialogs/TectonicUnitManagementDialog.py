from InProjectManagementDialog import *

from Gui.ItemModels.TectonicUnitItemModel import *
from Gui.ItemViews.TectonicUnitItemView import *

class TectonicUnitManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Tectonic Units'):
        InProjectManagementDialog.__init__(self, parent, project, 'Tectonic Units')
        self.addManagementWidget(TectonicUnitItemView)
        self.addCloseButton()
