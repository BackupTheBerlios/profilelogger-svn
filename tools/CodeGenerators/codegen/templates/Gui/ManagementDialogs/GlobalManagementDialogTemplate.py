from GlobalManagementDialog import *

from Gui.ItemModels.<class_name>ItemModel import *
from Gui.TreeViews.<class_name>TreeView import *

class <class_name>ManagementDialog(GlobalManagementDialog):
    def __init__(self, parent):
        GlobalManagementDialog.__init__(self, parent, <header>)
        self.addManagementWidget(<class_name>TreeView)
        self.addCloseButton()
