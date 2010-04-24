from InProjectManagementDialog import *

from Gui.ItemModels.OutcropTypeItemModel import *
from Gui.ItemViews.OutcropTypeItemView import *

class OutcropTypeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Outcrop Types'):
        InProjectManagementDialog.__init__(self, parent, project, 'Outcrop Types')
        self.addManagementWidget(OutcropTypeItemView)
        self.addCloseButton()
