from DataManagementItemView import DataManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.LithologicalUnitTypeItemModel import *

class LithologicalUnitTypeItemView(DataManagementItemView):
    def __init__(self, parent):
        DataManagementItemView.__init__(self, parent)
        self.configureModel(LithologicalUnitTypeItemModel(self))
