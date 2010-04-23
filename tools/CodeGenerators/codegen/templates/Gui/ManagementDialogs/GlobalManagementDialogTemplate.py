from ManagementDialog import *

from Gui.ItemModels.<class_name>ItemModel import *
from Gui.TreeViews.<class_name>TreeView import *

class <class_name>ManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent, <header>)
        self.addManagementWidget(<class_name>TreeView)
        self.addCloseButton()
