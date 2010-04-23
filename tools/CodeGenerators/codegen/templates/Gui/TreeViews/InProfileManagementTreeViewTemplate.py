from InProfileManagementTreeView import InProfileManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.<class_name>ItemModel import *

class <class_name>ItemView(InProfileManagementTreeView):
    def __init__(self, parent):
        InProfileManagementTreeView.__init__(self, parent)
        self.configureModel(<class_name>ItemModel(self))
