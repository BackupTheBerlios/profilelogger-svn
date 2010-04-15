from ManagementDialog import *

from Gui.ItemModels.GeologicalMeasurementTypeItemModel import *
from Gui.ItemViews.GeologicalMeasurementTypeItemView import *

class GeologicalMeasurementTypeManagementDialog(ManagementDialog):
    def __init__(self, parent):
        ManagementDialog.__init__(self, parent)
        self.addManagementWidget(GeologicalMeasurementTypeItemView)
        self.addCloseButton()
