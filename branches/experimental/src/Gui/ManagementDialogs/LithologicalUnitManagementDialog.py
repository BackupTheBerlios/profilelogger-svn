from DataInProjectManagementDialog import *

from Gui.ItemModels.LithologicalUnitItemModel import *
from Gui.ItemViews.LithologicalUnitItemView import *

class LithologicalUnitManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(LithologicalUnitItemView, LithologicalUnitItemModel)
        self.addCloseButton()
