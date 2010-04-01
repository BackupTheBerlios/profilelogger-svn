from DataInProjectSelectionComboBox import DataInProjectSelectionComboBox

from Gui.ManagementDialogs.BeddingTypeManagementDialog import *
from Persistance.BeddingTypeFinder import *

class BeddingTypeSelectionComboBox(DataInProjectSelectionComboBox):
    def __init__(self, parent):
        DataInProjectSelectionComboBox.__init__(self, parent, 
                                                BeddingTypeManagementDialog,
                                                BeddingTypeFinder)
        self.setToolTip(self.tr("Bedding Types"))
