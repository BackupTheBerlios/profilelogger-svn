from InProjectManagementDialog import *

from Gui.ItemModels.LithologyItemModel import *
from Gui.ItemViews.LithologyItemView import *

class LithologyManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Lithologies'):
        InProjectManagementDialog.__init__(self, parent, project, 'Lithologies')
        self.addManagementWidget(LithologyItemView)
        self.addCloseButton()
