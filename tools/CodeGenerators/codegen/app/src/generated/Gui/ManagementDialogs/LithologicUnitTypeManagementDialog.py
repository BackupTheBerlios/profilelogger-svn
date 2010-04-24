from InProjectManagementDialog import *

from Gui.ItemModels.LithologicUnitTypeItemModel import *
from Gui.ItemViews.LithologicUnitTypeItemView import *

class LithologicUnitTypeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Lithological Unit Types'):
        InProjectManagementDialog.__init__(self, parent, project, 'Lithological Unit Types')
        self.addManagementWidget(LithologicUnitTypeItemView)
        self.addCloseButton()
