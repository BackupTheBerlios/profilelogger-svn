from InProjectManagementDialog import *

from Gui.ItemModels.SedimentStructureItemModel import *
from Gui.ItemViews.SedimentStructureItemView import *

class SedimentStructureManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Sediment Structures'):
        InProjectManagementDialog.__init__(self, parent, project, 'Sediment Structures')
        self.addManagementWidget(SedimentStructureItemView)
        self.addCloseButton()
