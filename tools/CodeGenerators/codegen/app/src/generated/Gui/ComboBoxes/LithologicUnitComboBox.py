from InProjectComboBox import *

class LithologicUnitComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       LithologicUnitManagementDialog, 
                                       LithologicUnitFinder)
