from InProjectManagementTreeView import InProjectManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.<class_name>ItemModel import *

class <class_name>ItemView(InProjectManagementTreeView):
    def __init__(self, parent):
        InProjectManagementTreeView.__init__(self, parent)
        self.configureModel(<class_name>ItemModel(self))
