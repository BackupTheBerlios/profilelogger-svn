from InProjectManagementDialog import *

from Gui.ItemModels.StratigraphicUnitItemModel import *
from Gui.ItemViews.StratigraphicUnitItemView import *

class StratigraphicUnitManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Stratigraphic Units'):
        InProjectManagementDialog.__init__(self, parent, project, 'Stratigraphic Units')
        self.addManagementWidget(StratigraphicUnitItemView)
        self.addCloseButton()
