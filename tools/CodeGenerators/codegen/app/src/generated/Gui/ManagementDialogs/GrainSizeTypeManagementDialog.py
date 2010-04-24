from InProjectManagementDialog import *

from Gui.ItemModels.GrainSizeTypeItemModel import *
from Gui.ItemViews.GrainSizeTypeItemView import *

class GrainSizeTypeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Grain Size Types'):
        InProjectManagementDialog.__init__(self, parent, project, 'Grain Size Types')
        self.addManagementWidget(GrainSizeTypeItemView)
        self.addCloseButton()
