from DataInProjectManagementItemView import DataInProjectManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.CustomSymbolItemModel import *

class CustomSymbolItemView(DataInProjectManagementItemView):
    def __init__(self, parent):
        DataInProjectManagementItemView.__init__(self, parent)
        self.configureModel(CustomSymbolItemModel(self))
