from DataInProjectManagementItemView import DataInProjectManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.FaciesItemModel import *

class FaciesItemView(DataInProjectManagementItemView):
    def __init__(self, parent):
        DataInProjectManagementItemView.__init__(self, parent)
        self.configureModel(FaciesItemModel(self))
