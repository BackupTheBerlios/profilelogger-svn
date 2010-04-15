from ManagementDialog import *

from Gui.ItemModels.ProfileColumnItemModel import *
from Gui.ItemViews.ProfileColumnItemView import *

class ProfileColumnManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(ProfileColumnItemView)
        self.addCloseButton()
