from DataInBedManagementItemView import DataInBedManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.LithologicalUnitInBedItemModel import *

class LithologicalUnitInBedItemView(DataInBedManagementItemView):
    def __init__(self, parent):
        DataInBedManagementItemView.__init__(self, parent)
        self.configureModel(LithologicalUnitInBedItemModel(self))
