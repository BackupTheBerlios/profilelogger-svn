from InBedManagementTreeView import InBedManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.FossilInBedItemModel import *

class FossilInBedItemView(InBedManagementTreeView):
    def __init__(self, parent):
        InBedManagementTreeView.__init__(self, parent)
        self.configureModel(FossilInBedItemModel(self))