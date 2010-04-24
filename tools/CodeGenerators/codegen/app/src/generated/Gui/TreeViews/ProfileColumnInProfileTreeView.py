from InProfileManagementTreeView import InProfileManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.ProfileColumnInProfileItemModel import *

class ProfileColumnInProfileItemView(InProfileManagementTreeView):
    def __init__(self, parent):
        InProfileManagementTreeView.__init__(self, parent)
        self.configureModel(ProfileColumnInProfileItemModel(self))
