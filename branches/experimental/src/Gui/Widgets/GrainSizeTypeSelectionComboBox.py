from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.GrainSizeTypeManagementDialog import *
from Persistance.GrainSizeTypeFinder import *

class GrainSizeTypeSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       GrainSizeTypeManagementDialog,
                                       GrainSizeTypeFinder)
