from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.OutcropTypeManagementDialog import *
from Persistance.OutcropTypeFinder import *

class OutcropTypeSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                OutcropTypeManagementDialog,
                                                OutcropTypeFinder)
