from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.FossilManagementDialog import *
from Persistance.FossilFinder import *

class FossilSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                FossilManagementDialog,
                                                FossilFinder)
        self.setToolTip(self.tr("Fossils"))
