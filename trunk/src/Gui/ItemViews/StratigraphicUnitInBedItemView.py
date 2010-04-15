from DataInBedManagementItemView import DataInBedManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.StratigraphicUnitInBedItemModel import *

class StratigraphicUnitInBedItemView(DataInBedManagementItemView):
    def __init__(self, parent):
        DataInBedManagementItemView.__init__(self, parent)
        self.configureModel(StratigraphicUnitInBedItemModel(self))
