from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.TectonicUnitManagementDialog import *
from Persistance.TectonicUnitFinder import *

class TectonicUnitSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                TectonicUnitManagementDialog,
                                                TectonicUnitFinder)
        self.setToolTip(self.tr("Tectonic Units"))
