from DataInProjectManagementDialog import *

from Gui.ItemModels.BoundaryTypeItemModel import *
from Gui.ItemViews.BoundaryTypeItemView import *

class BoundaryTypeManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(BoundaryTypeItemView)
        self.addCloseButton()
