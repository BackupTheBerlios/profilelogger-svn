from InBedManagementTreeView import InBedManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.StratigraphicUnitInBedItemModel import *

class StratigraphicUnitInBedItemView(InBedManagementTreeView):
    def __init__(self, parent):
        InBedManagementTreeView.__init__(self, parent)
        self.configureModel(StratigraphicUnitInBedItemModel(self))
