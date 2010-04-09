from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.BoundaryTypeManagementDialog import *
from Persistance.BoundaryTypeFinder import *

class BoundaryTypeSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                BoundaryTypeManagementDialog,
                                                BoundaryTypeFinder)
        self.setToolTip(self.tr("Boundary Types"))
