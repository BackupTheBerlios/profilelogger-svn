from InProjectManagementDialog import *

from Gui.ItemModels.FaciesItemModel import *
from Gui.ItemViews.FaciesItemView import *

class FaciesManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Facies'):
        InProjectManagementDialog.__init__(self, parent, project, 'Facies')
        self.addManagementWidget(FaciesItemView)
        self.addCloseButton()
