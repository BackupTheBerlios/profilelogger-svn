from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.LengthUnitManagementDialog import *
from Persistance.LengthUnitFinder import *

class LengthUnitSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       LengthUnitManagementDialog,
                                       LengthUnitFinder)
        self.setToolTip(self.tr("Length Units"))
