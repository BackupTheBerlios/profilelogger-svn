from DataInProjectManagementDialog import *

from Gui.ItemModels.StratigraphicUnitItemModel import *
from Gui.ItemViews.StratigraphicUnitItemView import *

class StratigraphicUnitManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(StratigraphicUnitItemView, StratigraphicUnitItemModel)
        self.addCloseButton()
