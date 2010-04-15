from DataInProjectManagementDialog import *

from Gui.ItemModels.ColorItemModel import *
from Gui.ItemViews.ColorItemView import *

class ColorManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(ColorItemView)
        self.addCloseButton()
