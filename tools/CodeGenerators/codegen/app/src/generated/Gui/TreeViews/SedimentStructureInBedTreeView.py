from InBedManagementTreeView import InBedManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.SedimentStructureInBedItemModel import *

class SedimentStructureInBedItemView(InBedManagementTreeView):
    def __init__(self, parent):
        InBedManagementTreeView.__init__(self, parent)
        self.configureModel(SedimentStructureInBedItemModel(self))
