from InFieldBookManagementDialog import *

from Gui.ItemModels.<class_name>ItemModel import *
from Gui.ItemViews.<class_name>ItemView import *

class <class_name>ManagementDialog(InFieldBookManagementDialog):
    def __init__(self, parent, fieldBook, <header>):
        InFieldBookManagementDialog.__init__(self, parent, fieldBook, <header>)
        self.addManagementWidget(<class_name>ItemView)
        self.addCloseButton()
