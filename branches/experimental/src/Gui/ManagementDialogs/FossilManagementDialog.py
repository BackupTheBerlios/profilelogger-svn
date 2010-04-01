from DataInProjectManagementDialog import *

from Gui.ItemModels.FossilItemModel import *
from Gui.ItemViews.FossilItemView import *

class FossilManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(FossilItemView, FossilItemModel)
        self.addCloseButton()
