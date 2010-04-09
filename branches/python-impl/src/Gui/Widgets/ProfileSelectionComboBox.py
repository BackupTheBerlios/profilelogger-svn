
from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.ProfileManagementDialog import *
from Persistance.ProfileFinder import *

class ProfileSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                ProfileManagementDialog,
                                                ProfileFinder)
        self.setToolTip(self.tr("Profiles"))
