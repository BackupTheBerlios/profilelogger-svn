from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.LithologicalUnitManagementDialog import *
from Persistance.LithologicalUnitFinder import *

class LithologicalUnitSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                LithologicalUnitManagementDialog,
                                                LithologicalUnitFinder)
        self.setToolTip(self.tr("Lithological Units"))
