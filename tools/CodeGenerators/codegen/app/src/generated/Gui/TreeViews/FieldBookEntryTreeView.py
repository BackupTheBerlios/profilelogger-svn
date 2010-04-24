from InFieldBookManagementTreeView import InFieldBookManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.FieldBookEntryItemModel import *

class FieldBookEntryItemView(InFieldBookManagementTreeView):
    def __init__(self, parent):
        InFieldBookManagementTreeView.__init__(self, parent)
        self.configureModel(FieldBookEntryItemModel(self))
