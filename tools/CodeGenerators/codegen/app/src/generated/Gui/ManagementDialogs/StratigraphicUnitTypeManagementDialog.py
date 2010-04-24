from InProjectManagementDialog import *

from Gui.ItemModels.StratigraphicUnitTypeItemModel import *
from Gui.ItemViews.StratigraphicUnitTypeItemView import *

class StratigraphicUnitTypeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Stratigraphic Unit Types'):
        InProjectManagementDialog.__init__(self, parent, project, 'Stratigraphic Unit Types')
        self.addManagementWidget(StratigraphicUnitTypeItemView)
        self.addCloseButton()
