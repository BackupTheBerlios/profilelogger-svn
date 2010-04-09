from DataInProjectManagementDialog import *

from Gui.ItemModels.LithologyItemModel import *
from Gui.ItemViews.LithologyItemView import *

class LithologyManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(LithologyItemView, LithologyItemModel)
        self.addCloseButton()
