from InProfileComboBox import *

class BedComboBox(InProfileComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       BedManagementDialog, 
                                       BedFinder)
