from InProjectManagementDialog import *

from Gui.ItemModels.SedimentologicUnitTypeItemModel import *
from Gui.ItemViews.SedimentologicUnitTypeItemView import *

class SedimentologicUnitTypeManagementDialog(InProjectManagementDialog):
    def __init__(self, parent, project, 'Sedimentologic Unit Types'):
        InProjectManagementDialog.__init__(self, parent, project, 'Sedimentologic Unit Types')
        self.addManagementWidget(SedimentologicUnitTypeItemView)
        self.addCloseButton()
