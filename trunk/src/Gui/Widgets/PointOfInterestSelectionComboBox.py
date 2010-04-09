from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.PointOfInterestManagementDialog import *
from Persistance.PointOfInterestFinder import *

class PointOfInterestSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                PointOfInterestManagementDialog,
                                                PointOfInterestFinder)
        self.setToolTip(self.tr("Points Of Interest"))
