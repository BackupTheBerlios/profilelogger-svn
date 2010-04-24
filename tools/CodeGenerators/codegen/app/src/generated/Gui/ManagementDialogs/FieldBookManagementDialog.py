from GlobalManagementDialog import *

from Gui.ItemModels.FieldBookItemModel import *
from Gui.TreeViews.FieldBookTreeView import *

class FieldBookManagementDialog(GlobalManagementDialog):
    def __init__(self, parent):
        GlobalManagementDialog.__init__(self, parent, 'Field Books')
        self.addManagementWidget(FieldBookTreeView)
        self.addCloseButton()
