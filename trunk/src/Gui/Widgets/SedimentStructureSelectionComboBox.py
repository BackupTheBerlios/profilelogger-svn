from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.SedimentStructureManagementDialog import *
from Persistance.SedimentStructureFinder import *

class SedimentStructureSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                SedimentStructureManagementDialog,
                                                SedimentStructureFinder)
        self.setToolTip(self.tr("Sediment Structures"))
