from DataInProjectManagementDialog import *

from Gui.ItemModels.FaciesItemModel import *
from Gui.ItemViews.FaciesItemView import *

class FaciesManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(FaciesItemView)
        self.addCloseButton()
