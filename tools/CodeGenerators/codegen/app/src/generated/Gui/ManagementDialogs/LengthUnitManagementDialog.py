from GlobalManagementDialog import *

from Gui.ItemModels.LengthUnitItemModel import *
from Gui.TreeViews.LengthUnitTreeView import *

class LengthUnitManagementDialog(GlobalManagementDialog):
    def __init__(self, parent):
        GlobalManagementDialog.__init__(self, parent, 'Length Units')
        self.addManagementWidget(LengthUnitTreeView)
        self.addCloseButton()
