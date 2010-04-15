from DataInProjectManagementDialog import *

from Gui.ItemModels.SedimentStructureItemModel import *
from Gui.ItemViews.SedimentStructureItemView import *

class SedimentStructureManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(SedimentStructureItemView)
        self.addCloseButton()
