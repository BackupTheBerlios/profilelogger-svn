from InProjectManagementDialog import *

from Gui.ItemModels.CustomSymbolItemModel import *
from Gui.ItemViews.CustomSymbolItemView import *

class CustomSymbolManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Custom Symbols'):
        InProjectManagementDialog.__init__(self, parent, project, 'Custom Symbols')
        self.addManagementWidget(CustomSymbolItemView)
        self.addCloseButton()
