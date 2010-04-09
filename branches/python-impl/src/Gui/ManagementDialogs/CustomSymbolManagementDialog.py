from DataInProjectManagementDialog import *

from Gui.ItemModels.CustomSymbolItemModel import *
from Gui.ItemViews.CustomSymbolItemView import *

class CustomSymbolManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(CustomSymbolItemView, CustomSymbolItemModel)
        self.addCloseButton()
