from InProfileManagementDialog import *

from Gui.ItemModels.ProfileColumnInProfileItemModel import *
from Gui.ItemViews.ProfileColumnInProfileItemView import *

class ProfileColumnInProfileManagementDialog(InProfileManagementDialog):
    def __init__(self, parent, profile, 'Profile Column In Profile'):
        InProfileManagementDialog.__init__(self, parent, profile, 'Profile Column In Profile')
        self.addManagementWidget(ProfileColumnInProfileItemView)
        self.addCloseButton()
