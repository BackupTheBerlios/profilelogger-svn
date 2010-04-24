from InBedComboBox import *

class LithologicUnitInBedComboBox(InBedComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       LithologicUnitInBedManagementDialog, 
                                       LithologicUnitInBedFinder)
