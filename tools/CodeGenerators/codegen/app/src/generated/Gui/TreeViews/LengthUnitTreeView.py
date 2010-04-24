from ManagementTreeView import ManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.LengthUnitItemModel import *

class LengthUnitItemView(ManagementTreeView):
    def __init__(self, parent):
        ManagementTreeView.__init__(self, parent)
        self.configureModel(LengthUnitItemModel(self))
