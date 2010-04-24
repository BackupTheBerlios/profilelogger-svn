from InProjectManagementDialog import *

from Gui.ItemModels.BoundaryTypeItemModel import *
from Gui.ItemViews.BoundaryTypeItemView import *

class BoundaryTypeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Boundary Types'):
        InProjectManagementDialog.__init__(self, parent, project, 'Boundary Types')
        self.addManagementWidget(BoundaryTypeItemView)
        self.addCloseButton()
