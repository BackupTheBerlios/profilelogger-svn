from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.GrainSizeManagementDialog import *
from Persistance.GrainSizeFinder import *

class GrainSizeSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       GrainSizeManagementDialog,
                                       GrainSizeFinder)
