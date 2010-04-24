from InProjectManagementDialog import *

from Gui.ItemModels.FossilItemModel import *
from Gui.ItemViews.FossilItemView import *

class FossilManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Fossils'):
        InProjectManagementDialog.__init__(self, parent, project, 'Fossils')
        self.addManagementWidget(FossilItemView)
        self.addCloseButton()
