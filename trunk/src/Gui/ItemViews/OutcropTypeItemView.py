from DataInProjectManagementItemView import DataInProjectManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.OutcropTypeItemModel import *

class OutcropTypeItemView(DataInProjectManagementItemView):
    def __init__(self, parent):
        DataInProjectManagementItemView.__init__(self, parent)
        self.configureModel(OutcropTypeItemModel(self))
