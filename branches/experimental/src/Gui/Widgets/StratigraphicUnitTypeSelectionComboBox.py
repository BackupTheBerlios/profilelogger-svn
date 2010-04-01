from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.StratigraphicUnitTypeManagementDialog import *
from Persistance.StratigraphicUnitTypeFinder import *

class StratigraphicUnitTypeSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       StratigraphicUnitTypeManagementDialog,
                                       StratigraphicUnitTypeFinder)
