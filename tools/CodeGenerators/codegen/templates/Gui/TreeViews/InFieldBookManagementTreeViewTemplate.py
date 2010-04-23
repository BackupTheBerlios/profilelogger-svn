from InFieldBookManagementTreeView import InFieldBookManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.<class_name>ItemModel import *

class <class_name>ItemView(InFieldBookManagementTreeView):
    def __init__(self, parent):
        InFieldBookManagementTreeView.__init__(self, parent)
        self.configureModel(<class_name>ItemModel(self))
