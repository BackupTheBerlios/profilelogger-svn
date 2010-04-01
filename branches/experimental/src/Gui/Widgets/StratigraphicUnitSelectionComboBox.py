from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.StratigraphicUnitManagementDialog import *
from Persistance.StratigraphicUnitFinder import *

class StratigraphicUnitSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                StratigraphicUnitManagementDialog,
                                                StratigraphicUnitFinder)
        self.setToolTip(self.tr("Stratigraphic Units"))
