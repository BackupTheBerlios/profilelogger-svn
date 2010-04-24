from InProfileManagementDialog import *

from Gui.ItemModels.ProfileColumnItemModel import *
from Gui.ItemViews.ProfileColumnItemView import *

class ProfileColumnManagementDialog(InProfileManagementDialog):
    def __init__(self, parent, profile, 'Profile Columns'):
        InProfileManagementDialog.__init__(self, parent, profile, 'Profile Columns')
        self.addManagementWidget(ProfileColumnItemView)
        self.addCloseButton()
