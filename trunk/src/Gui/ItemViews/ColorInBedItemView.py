from DataInBedManagementItemView import DataInBedManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.ColorInBedItemModel import *

class ColorInBedItemView(DataInBedManagementItemView):
    def __init__(self, parent):
        DataInBedManagementItemView.__init__(self, parent)
        self.configureModel(ColorInBedItemModel(self))
