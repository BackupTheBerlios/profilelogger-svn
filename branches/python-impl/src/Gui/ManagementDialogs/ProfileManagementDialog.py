from DataInProjectManagementDialog import *

from Gui.ItemModels.ProfileItemModel import *
from Gui.ItemViews.ProfileItemView import *

class ProfileManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(ProfileItemView, ProfileItemModel)
        self.addCloseButton()
