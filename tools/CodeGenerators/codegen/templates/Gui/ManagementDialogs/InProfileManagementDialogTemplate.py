from InProfileManagementDialog import *

from Gui.ItemModels.<class_name>ItemModel import *
from Gui.ItemViews.<class_name>ItemView import *

class <class_name>ManagementDialog(InProfileManagementDialog):
    def __init__(self, parent, profile, <header>):
        InProfileManagementDialog.__init__(self, parent, profile, <header>)
        self.addManagementWidget(<class_name>ItemView)
        self.addCloseButton()
