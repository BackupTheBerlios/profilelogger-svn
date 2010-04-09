from DataInProjectManagementDialog import *

from Gui.ItemModels.PointOfInterestItemModel import *
from Gui.ItemViews.PointOfInterestItemView import *

class PointOfInterestManagementDialog(DataInProjectManagementDialog):
    def __init__(self, parent, project):
        DataInProjectManagementDialog.__init__(self, parent, project)
        self.addManagementWidget(PointOfInterestItemView, PointOfInterestItemModel)
        self.addCloseButton()
