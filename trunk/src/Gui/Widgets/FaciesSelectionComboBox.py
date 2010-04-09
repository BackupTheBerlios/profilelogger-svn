from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.FaciesManagementDialog import *
from Persistance.FaciesFinder import *

class FaciesSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                FaciesManagementDialog,
                                                FaciesFinder)
        self.setToolTip(self.tr("Facies"))
