from InProjectManagementDialog import *

from Gui.ItemModels.ColorItemModel import *
from Gui.ItemViews.ColorItemView import *

class ColorManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Colors'):
        InProjectManagementDialog.__init__(self, parent, project, 'Colors')
        self.addManagementWidget(ColorItemView)
        self.addCloseButton()
