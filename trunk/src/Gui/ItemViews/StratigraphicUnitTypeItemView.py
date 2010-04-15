from DataManagementItemView import DataManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.StratigraphicUnitTypeItemModel import *

class StratigraphicUnitTypeItemView(DataManagementItemView):
    def __init__(self, parent):
        DataManagementItemView.__init__(self, parent)
        self.configureModel(StratigraphicUnitTypeItemModel(self))
