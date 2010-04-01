from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.ColorManagementDialog import *
from Persistance.ColorFinder import *

class ColorSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                ColorManagementDialog,
                                                ColorFinder)
