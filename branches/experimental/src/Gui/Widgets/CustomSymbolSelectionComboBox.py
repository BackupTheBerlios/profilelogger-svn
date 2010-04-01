from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.CustomSymbolManagementDialog import *
from Persistance.CustomSymbolFinder import *

class CustomSymbolSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                CustomSymbolManagementDialog,
                                                CustomSymbolFinder)
