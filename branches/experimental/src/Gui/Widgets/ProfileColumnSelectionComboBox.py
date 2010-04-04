from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.ProfileColumnManagementDialog import *
from Persistance.ProfileColumnFinder import *

class ProfileColumnSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       ProfileColumnManagementDialog,
                                       ProfileColumnFinder)
        self.setToolTip(self.tr("Profile Columns"))
