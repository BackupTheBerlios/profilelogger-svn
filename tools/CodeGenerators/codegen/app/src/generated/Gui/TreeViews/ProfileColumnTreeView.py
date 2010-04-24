from InProfileManagementTreeView import InProfileManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.ProfileColumnItemModel import *

class ProfileColumnItemView(InProfileManagementTreeView):
    def __init__(self, parent):
        InProfileManagementTreeView.__init__(self, parent)
        self.configureModel(ProfileColumnItemModel(self))
