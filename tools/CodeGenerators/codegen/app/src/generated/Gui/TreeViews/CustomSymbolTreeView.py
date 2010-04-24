from InProjectManagementTreeView import InProjectManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.CustomSymbolItemModel import *

class CustomSymbolItemView(InProjectManagementTreeView):
    def __init__(self, parent):
        InProjectManagementTreeView.__init__(self, parent)
        self.configureModel(CustomSymbolItemModel(self))