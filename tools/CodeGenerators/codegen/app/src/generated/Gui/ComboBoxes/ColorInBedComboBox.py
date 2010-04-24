from InBedComboBox import *

class ColorInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       ColorInBedManagementDialog, 
                                       ColorInBedFinder)
