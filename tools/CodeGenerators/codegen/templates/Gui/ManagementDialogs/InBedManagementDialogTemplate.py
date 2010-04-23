from InBedManagementDialog import *

from Gui.ItemModels.<class_name>ItemModel import *
from Gui.ItemViews.<class_name>ItemView import *

class <class_name>ManagementDialog(InBedManagementDialog):
    def __init__(self, parent, bed, <header>):
        InBedManagementDialog.__init__(self, parent, bed, <header>)
        self.addManagementWidget(<class_name>ItemView)
        self.addCloseButton()
