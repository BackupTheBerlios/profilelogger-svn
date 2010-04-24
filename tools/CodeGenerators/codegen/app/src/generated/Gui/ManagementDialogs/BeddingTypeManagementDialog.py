from InProjectManagementDialog import *

from Gui.ItemModels.BeddingTypeItemModel import *
from Gui.ItemViews.BeddingTypeItemView import *

class BeddingTypeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Bedding Types'):
        InProjectManagementDialog.__init__(self, parent, project, 'Bedding Types')
        self.addManagementWidget(BeddingTypeItemView)
        self.addCloseButton()
