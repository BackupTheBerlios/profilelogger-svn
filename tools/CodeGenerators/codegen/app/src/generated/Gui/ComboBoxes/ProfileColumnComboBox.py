from InProfileComboBox import *

class ProfileColumnComboBox(InProfileComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       ProfileColumnManagementDialog, 
                                       ProfileColumnFinder)
