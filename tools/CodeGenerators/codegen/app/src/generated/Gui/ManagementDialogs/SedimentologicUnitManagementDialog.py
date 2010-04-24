from InProjectManagementDialog import *

from Gui.ItemModels.SedimentologicUnitItemModel import *
from Gui.ItemViews.SedimentologicUnitItemView import *

class SedimentologicUnitManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Sedimentologic Units'):
        InProjectManagementDialog.__init__(self, parent, project, 'Sedimentologic Units')
        self.addManagementWidget(SedimentologicUnitItemView)
        self.addCloseButton()
