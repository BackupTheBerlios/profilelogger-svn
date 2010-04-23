from InProjectManagementDialog import *

from Gui.ItemModels.<class_name>ItemModel import *
from Gui.ItemViews.<class_name>ItemView import *

class <class_name>ManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, <header>):
        InProjectManagementDialog.__init__(self, parent, project, <header>)
        self.addManagementWidget(<class_name>ItemView)
        self.addCloseButton()
