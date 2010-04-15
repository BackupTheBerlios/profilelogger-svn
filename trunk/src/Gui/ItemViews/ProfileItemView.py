from DataInProjectManagementItemView import DataInProjectManagementItemView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui import *

class ProfileItemView(DataInProjectManagementItemView):
    def __init__(self, parent):
        DataInProjectManagementItemView.__init__(self, parent)
        self.configureModel(ItemModels.ProfileItemModel.ProfileItemModel(self))
