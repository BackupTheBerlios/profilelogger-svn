from DataManagementItemView import DataManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.GrainSizeTypeItemModel import *

class GrainSizeTypeItemView(DataManagementItemView):
    def __init__(self, parent):
        DataManagementItemView.__init__(self, parent)
        self.configureModel(GrainSizeTypeItemModel(self))
