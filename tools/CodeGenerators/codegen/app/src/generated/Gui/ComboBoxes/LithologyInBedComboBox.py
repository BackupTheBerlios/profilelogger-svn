from InBedComboBox import *

class LithologyInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       LithologyInBedManagementDialog, 
                                       LithologyInBedFinder)
