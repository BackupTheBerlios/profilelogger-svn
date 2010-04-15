from DataInProjectManagementDialog import *

from Gui.ItemModels.OutcropTypeItemModel import *
from Gui.ItemViews.OutcropTypeItemView import *

class OutcropTypeManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(OutcropTypeItemView)
        self.addCloseButton()
