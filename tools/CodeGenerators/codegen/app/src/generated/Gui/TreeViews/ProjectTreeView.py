from ManagementTreeView import ManagementTreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui.ItemModels.ProjectItemModel import *

class ProjectItemView(ManagementTreeView):
    def __init__(self, parent):
        ManagementTreeView.__init__(self, parent)
        self.configureModel(ProjectItemModel(self))
