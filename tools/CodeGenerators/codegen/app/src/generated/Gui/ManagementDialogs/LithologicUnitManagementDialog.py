from InProjectManagementDialog import *

from Gui.ItemModels.LithologicUnitItemModel import *
from Gui.ItemViews.LithologicUnitItemView import *

class LithologicUnitManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Lithological Units'):
        InProjectManagementDialog.__init__(self, parent, project, 'Lithological Units')
        self.addManagementWidget(LithologicUnitItemView)
        self.addCloseButton()
