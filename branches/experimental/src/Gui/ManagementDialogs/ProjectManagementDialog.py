from ManagementDialog import *

from Gui.ItemModels.ProjectItemModel import *
from Gui.ItemViews.ProjectItemView import *

class ProjectManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(ProjectItemView, ProjectItemModel)
        self.addCloseButton()
