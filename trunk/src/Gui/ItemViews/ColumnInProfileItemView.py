from DataInProfileManagementItemView import DataInProfileManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.ColumnInProfileItemModel import *

class ColumnInProfileItemView(DataInProfileManagementItemView):
    def __init__(self, parent):
        DataInProfileManagementItemView.__init__(self, parent)
        self.configureModel(ColumnInProfileItemModel(self))
