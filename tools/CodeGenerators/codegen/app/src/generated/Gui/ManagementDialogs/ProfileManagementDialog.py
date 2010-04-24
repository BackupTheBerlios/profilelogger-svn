from InProjectManagementDialog import *

from Gui.ItemModels.ProfileItemModel import *
from Gui.ItemViews.ProfileItemView import *

class ProfileManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Profiles'):
        InProjectManagementDialog.__init__(self, parent, project, 'Profiles')
        self.addManagementWidget(ProfileItemView)
        self.addCloseButton()
