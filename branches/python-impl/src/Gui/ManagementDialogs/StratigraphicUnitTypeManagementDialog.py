from ManagementDialog import *

from Gui.ItemModels.StratigraphicUnitTypeItemModel import *
from Gui.ItemViews.StratigraphicUnitTypeItemView import *

class StratigraphicUnitTypeManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(StratigraphicUnitTypeItemView, StratigraphicUnitTypeItemModel)
        self.addCloseButton()
