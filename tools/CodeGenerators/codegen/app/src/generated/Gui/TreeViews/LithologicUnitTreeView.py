from InProjectManagementTreeView import InProjectManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.LithologicUnitItemModel import *

class LithologicUnitItemView(InProjectManagementTreeView):
    def __init__(self, parent):
        InProjectManagementTreeView.__init__(self, parent)
        self.configureModel(LithologicUnitItemModel(self))
