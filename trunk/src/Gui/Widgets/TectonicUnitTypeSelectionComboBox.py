from DataSelectionComboBox import DataSelectionComboBox

from Gui.ManagementDialogs.TectonicUnitTypeManagementDialog import *
from Persistance.TectonicUnitTypeFinder import *

class TectonicUnitTypeSelectionComboBox(DataSelectionComboBox):
    def __init__(self, parent):
        DataSelectionComboBox.__init__(self, parent, 
                                       TectonicUnitTypeManagementDialog,
                                       TectonicUnitTypeFinder)
        self.setToolTip(self.tr("Tectonic Unit Types"))
