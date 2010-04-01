from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.ProjectManagementDialog import *
from Persistance.ProjectFinder import *

class ProjectSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       ProjectManagementDialog,
                                       ProjectFinder)
