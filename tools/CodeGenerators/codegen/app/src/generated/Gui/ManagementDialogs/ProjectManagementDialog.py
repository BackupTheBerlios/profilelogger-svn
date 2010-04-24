from GlobalManagementDialog import *

from Gui.ItemModels.ProjectItemModel import *
from Gui.TreeViews.ProjectTreeView import *

class ProjectManagementDialog(GlobalManagementDialog):
    def __init__(self, parent):
        GlobalManagementDialog.__init__(self, parent, 'Projects')
        self.addManagementWidget(ProjectTreeView)
        self.addCloseButton()
