from InProfileComboBox import *

class ProfileColumnInProfileComboBox(InProfileComboBox):
    def __init__(self, parent, managementDialogClass, finderClass):
        DataSelectionComboBox.__init__(self, 
                                       parent, 
                                       ProfileColumnInProfileManagementDialog, 
                                       ProfileColumnInProfileFinder)
