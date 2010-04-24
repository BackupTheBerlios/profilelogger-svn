from InProjectComboBox import *

class ProfileComboBox(InProjectComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       ProfileManagementDialog, 
                                       ProfileFinder)
