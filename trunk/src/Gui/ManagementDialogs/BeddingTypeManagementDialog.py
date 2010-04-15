from DataInProjectManagementDialog import *

from Gui.ItemModels.BeddingTypeItemModel import *
from Gui.ItemViews.BeddingTypeItemView import *

class BeddingTypeManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(BeddingTypeItemView)
        self.addCloseButton()
