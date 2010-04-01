from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.LithologyManagementDialog import *
from Persistance.LithologyFinder import *

class LithologySelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                LithologyManagementDialog,
                                                LithologyFinder)
