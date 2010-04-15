from DataInProjectManagementDialog import *

from Gui.ItemModels.ProfileAssemblyItemModel import *
from Gui.ItemViews.ProfileAssemblyItemView import *

class ProfileAssemblyManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(ProfileAssemblyItemView)
        self.addCloseButton()
