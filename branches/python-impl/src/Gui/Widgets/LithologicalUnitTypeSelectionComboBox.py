from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.LithologicalUnitTypeManagementDialog import *
from Persistance.LithologicalUnitTypeFinder import *

class LithologicalUnitTypeSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       LithologicalUnitTypeManagementDialog,
                                       LithologicalUnitTypeFinder)
        self.setToolTip(self.tr("Lithological Unit Types"))
