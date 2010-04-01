
from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.ProfileAssemblyManagementDialog import *
from Persistance.ProfileAssemblyFinder import *

class ProfileAssemblySelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                ProfileAssemblyManagementDialog,
                                                ProfileAssemblyFinder)
